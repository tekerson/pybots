let
    pkgs = import <nixpkgs> {};
    stdenv = pkgs.stdenv;
in rec {
    python27DevEnv = pkgs.myEnvFun {
        name = "python27-dev";
        buildInputs = with pkgs; [
            python27Full
            python27Packages.nose
        ];
    };
}
