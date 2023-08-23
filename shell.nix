{ pkgs ? import <nixpkgs> {}}:

pkgs.mkShell {
  nativeBuildInputs = [
    pkgs.python3Full
    pkgs.python3Packages.mkdocs
    pkgs.python3Packages.mkdocs-material
    pkgs.python3Packages.pip-tools
  ];
}
