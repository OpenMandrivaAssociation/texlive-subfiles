%global tl_name subfiles
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Individual typesetting of subfiles of a main document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/subfiles
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subfiles.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subfiles.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subfiles.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(import)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Using this package the user can handle multi-file projects more
comfortably, making it possible to both process the subsidiary files by
themselves and to process the main file that includes them, without
making any changes to either.

