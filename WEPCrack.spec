%include	/usr/lib/rpm/macros.perl
Summary:	Tool that cracks 802.11 WEP encryption keys
Summary(pl):	Program do ³amania szyfrowania WEP dla protoko³u 802.11
Name:		WEPCrack
Version:	0.1.0
Release:	1
License:	GPL
Group:		Networking
Source0:	http://dl.sourceforge.net/wepcrack/%{name}-%{version}.tar.gz
# Source0-md5:	bbab3f07c8b47ac275459320f698711a
# Source0-size:	6277
URL:		http://sourceforge.net/projects/wepcrack/
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WEPCrack is a tool that cracks 802.11 WEP encryption keys using the
latest discovered weakness of RC4 key scheduling.

%description -l pl
WEPCrack to program do ³amania szyfrowania WEP dla protoko³u 802.11,
przy u¿yciu luki znalezionej w kluczach RC4.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install pcap-getIV.pl WeakIVGen.pl WEPCrack.pl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
