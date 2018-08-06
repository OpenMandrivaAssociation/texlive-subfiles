# revision 26645
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-subfiles
Version:	1.2
Release:	1
Summary:	TeXLive subfiles package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfiles.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfiles.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfiles.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120810-1
+ Revision: 813772
- Import texlive-subfiles
- Import texlive-subfiles

