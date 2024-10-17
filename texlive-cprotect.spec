Name:		texlive-cprotect
Version:	21209
Release:	2
Summary:	Allow verbatim, etc., in macro arguments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cprotect
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cprotect.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cprotect.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cprotect.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines the macro \cprotect that makes a following
macro proof against verbatim in its argument; as, for example,
\cprotect\section{\verb"foo"} A similar macro \cprotEnv
(applied to the \begin of an environment) sanitises the
behavior of fragile environments. Moving arguments, and
corresponding "tables of ..." work happily.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cprotect/cprotect.sty
%doc %{_texmfdistdir}/doc/latex/cprotect/README
%doc %{_texmfdistdir}/doc/latex/cprotect/README.txt
%doc %{_texmfdistdir}/doc/latex/cprotect/cprotect.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cprotect/cprotect.dtx
%doc %{_texmfdistdir}/source/latex/cprotect/cprotect.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
