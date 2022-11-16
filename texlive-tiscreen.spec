Name:		texlive-tiscreen
Version:	62602
Release:	1
Summary:	Mimic the screen of older Texas Instruments calculators
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tiscreen
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tiscreen.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tiscreen.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package mimics the screen of older Texas Instruments dot
matrix display calculators, specifically the TI-82 STATS. It
relies on the lcd and xcolor packages.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tiscreen
%doc %{_texmfdistdir}/doc/latex/tiscreen

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
