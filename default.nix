with import <nixpkgs> {};
stdenv.mkDerivation rec {
  name = "env";
  env = buildEnv { name = name; paths = buildInputs; };
  
  buildInputs = [
    python
    python27Packages.pip
    python27Packages.docopt
    python27Packages.pyyaml
    python27Packages.feedparser
    ];
}
