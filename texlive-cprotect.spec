%global tl_name cprotect
%global tl_revision 78728

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0f
Release:	%{tl_revision}.1
Summary:	Allow verbatim, etc., in macro arguments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cprotect
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cprotect.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cprotect.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cprotect.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(bigfoot)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines the macro \cprotect that makes a following macro
proof against verbatim in its argument; as, for example,
\cprotect\section{\verb"foo"} A similar macro \cprotEnv (applied to the
\begin of an environment) sanitises the behavior of fragile
environments. Moving arguments, and corresponding "tables of ..." work
happily.

