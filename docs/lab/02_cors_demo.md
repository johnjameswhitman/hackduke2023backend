# 02 CORS Demo

## Intro

The idea behind CORS is to guard your API against unauthorized requests from 
third party sites. For example, imagine you're developing an API for a bank. You
would want to prevent an evil website from embedding some javascript on 
their site that calls the bank's API using the customer's session credentials 
while they're logged into the bank from a different tab.

To avoid this situation, all browsers respect a special 
`access-control-allow-origin` header that your API sends back in responses. 
This provides a list of _origins_ whose javascript the browser should allow 
to make requests to the API. Origins are defined as the combination of 
`protocol://domain:port`.

![CORS header](02_cors_demo/cors_header.png "cors header")

The API configures the `access-control-allow-origin` header within
[`config/settings.py`](https://github.com/johnjameswhitman/hackduke2023backend/blob/0f05f07e08af798ea1aea85a10734f5433dee29c/config/settings.py#L31-L33)
as follows:

```python
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8001",  # Docs site
    "http://mealpointsapp.localhost:8001",  # CORS demo site
]
```

So, if you wanted to allow AJAX (i.e. javascript) requests from a React.js 
front-end hosted on a different origin than your API, you would need to add 
that to your project's settings.

## Setup

Let's demo CORS with the local API. It will work if you're viewing this page
from a development mkdocs server running from an origin of
`http://mealpointsapp.localhost:8001`...

- You're currently viewing this page from the origin: <pre id="corsDemoLocation">thinking...</pre>
- Therefore, the API will <b id="corsDemoAccept">thinking...</b> your 
  request.

## Demo

Below is a form that'll transfer some "meal points" using a dummy endpoint in 
the API. Let's try it from two different _origins_. Open each of these links in
different tabs and then click _Transfer_ below:

- [`http://mealpointsapp.localhost:8001/lab/02_cors_demo/`](http://127.0.0.1:8001/lab/02_cors_demo/#demo)
- [`http://badguys.localhost:8001/lab/02_cors_demo/`](http://badguys.localhost:8001/lab/02_cors_demo/#demo)

!!! Note

    `mealpointsapp.localhost` and `badguys.localhost` are both addresses that
    point back to your local machine; however, because they're different 
    domains each address represents a different _origin_.

### Transfer "meal points"

<form>
  <input id="corsDemoInputAmount" class="md-input" placeholder="Points" value="100"/>
  <input id="corsDemoInputDestination" class="md-input" placeholder="Who" value="Blue Devil"/>
  <button id="corsDemoButton" class="md-button md-button--primary" type="button">Transfer</button>
</form>

If you submit the above for from an allowed origin, then you should get an 
alert:

![CORS accepted](02_cors_demo/accepted_alert.png "cors accepted")

But, if you submit it from a disallowed origin, then you'll get an error and 
should see something like below in your browser console:

![CORS rejected](02_cors_demo/rejected_console.png "cors rejected")

<script>
  (() => {
    let httpRequest;
    document
      .getElementById("corsDemoButton")
      .addEventListener("click", makeRequest);

    function makeRequest() {
      httpRequest = new XMLHttpRequest();

      if (!httpRequest) {
        alert("Giving up :( Cannot create an XMLHTTP instance");
        return false;
      }
      httpRequest.addEventListener("load", transferComplete);
      httpRequest.addEventListener("error", transferFailed);
      httpRequest.open("POST", "http://127.0.0.1:8000/api/auth/cors_demo");
      httpRequest.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
      httpRequest.send(
        JSON.stringify(
          {
            "amount": document.getElementById("corsDemoInputAmount").value, 
            "destination": document.getElementById("corsDemoInputDestination").value,
          }
        )
      );
    }

    function transferComplete(evt) {
      alert(evt.target.responseText);
    }

    function transferFailed(evt) {
      alert("Request failed! CORS issue?");
    }

    function locationCorsApproved() {
      const allowedIP = /^http:\/\/127\.0\.0\.1:8001\//;
      const allowedDomain = /^http:\/\/mealpointsapp\.localhost:8001\//;
      document.getElementById("corsDemoLocation").innerText = `${window.location.protocol}//${window.location.host}`;
      if (allowedIP.test(window.location) || allowedDomain.test(window.location)) {
        document.getElementById("corsDemoAccept").innerText = "accept ✅";
      } else {
        document.getElementById("corsDemoAccept").innerText = "reject ❌";
      }
    }

    locationCorsApproved();
  })();
</script>
