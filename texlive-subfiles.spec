Name:		texlive-subfiles
Version:	56977
Release:	2
Summary:	TeXLive subfiles package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfiles.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfiles.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfiles.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive subfiles package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/subfiles/subfiles.cls
%{_texmfdistdir}/tex/latex/subfiles/subfiles.sty
%doc %{_texmfdistdir}/doc/latex/subfiles/README
%doc %{_texmfdistdir}/doc/latex/subfiles/subfiles.pdf
#- source
%doc %{_texmfdistdir}/source/latex/subfiles/subfiles.dtx
%doc %{_texmfdistdir}/source/latex/subfiles/subfiles.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
