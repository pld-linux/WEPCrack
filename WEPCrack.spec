%include        /usr/lib/rpm/macros.perl
Summary:	Tool that cracks 802.11 WEP encryption keys.
Summary(pl):	Program do ³amania szyfrowania WEP dla protoko³u 802.11.
Name:		WEPCrack
Version:	0.0.10
Release:	1
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/wepcrack/%{name}-%{version}.tar.gz
# Source0-md5:	d95af657c629e0c10c90a375a0f7f2c7
URL:		http://sourceforge.net/projects/webcrack/
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WEPCrack is a tool that cracks 802.11 WEP encryption keys using the
latest discovered weakness of RC4 key scheduling.

%description -l pl
WEPCrack to program do ³amania szydrowania WEP dla protoko³u 802.11,
uu¿ywaj±c luki znalezionej w kluczach RC4.

%prep
%setup -q -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install prism-decode.pl prism-getIV.pl WeakIVGen.pl WEPCrack.pl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
