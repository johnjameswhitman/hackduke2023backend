{ pkgs ? import <nixpkgs> {}}:

pkgs.mkShell {
  nativeBuildInputs = [
    pkgs.mkdocs
    pkgs.python3Full
    pkgs.python3Packages.pip-tools
  ];
}
