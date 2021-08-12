# generated by cabal-rpm-2.0.10
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

Name:           koji-install
Version:        0.1.0
Release:        1%{?dist}
Summary:        CLI tool for installing rpms directly from Fedora Koji

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-static
BuildRequires:  ghc-directory-static
BuildRequires:  ghc-extra-static
BuildRequires:  ghc-filepath-static
BuildRequires:  ghc-koji-static
BuildRequires:  ghc-rpm-nvr-static
BuildRequires:  ghc-simple-cmd-static
BuildRequires:  ghc-simple-cmd-args-static
BuildRequires:  ghc-xdg-userdirs-static
# End cabal-rpm deps

%description
koji-install can install the latest koji build of a package locally.
By default it only downloads newer binaries of the subpackages
already installed, but there are options to override that.


%prep
# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_bin_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_bin_install
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
%{buildroot}%{_bindir}/%{name} --bash-completion-script %{name} | sed s/filenames/default/ > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
# End cabal-rpm install


%files
# Begin cabal-rpm files:
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
# End cabal-rpm files


%changelog
* Thu Aug 12 2021 Jens Petersen <petersen@redhat.com> - 0.1.0-1
- spec file generated by cabal-rpm-2.0.10