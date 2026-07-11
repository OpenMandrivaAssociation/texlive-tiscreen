%global tl_name tiscreen
%global tl_revision 62602

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Mimic the screen of older Texas Instruments calculators
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tiscreen
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tiscreen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tiscreen.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package mimics the screen of older Texas Instruments dot matrix
display calculators, specifically the TI-82 STATS. It relies on the lcd
and xcolor packages.

