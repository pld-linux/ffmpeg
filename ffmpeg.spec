Summary:	realtime audio/video encoder and streaming server
Summary(pl):	koder audio/wideo czasu rzeczywistego oraz serwer strumieni
Name:		ffmpeg
Version:	0.4.4
Release:	1
License:	GPL
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
Source0:	http://prdownloads.sourceforge.net/ffmpeg/%{name}-%{version}.tar.gz
URL:		http://ffmpeg.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:  nasm

%description
ffmpeg is a hyper fast realtime audio/video encoder and streaming
server. It can grab from a standard Video4Linux video source and
convert it into several file formats based on DCT/motion compensation
encoding. Sound is compressed in MPEG audio layer 2 or using an AC3
compatible stream.

%description -l pl
ffmpeg jest bardzo szybkim koderem audio/wideo w czasie rzeczywistym
oraz serwerem strumieni multimedialnych. ffmpeg potrafi zrzucaæ dane
ze standardowego urz±dzenia Video4Linux i przekonwertowaæ je w kilka
formatów plików bazuj±cych na kodowaniu DCT/kompensacyji ruchu. Dzwiêk
jest kompresowany do strumienia MPEG audio layer 2 lub u¿ywaj±c
strumienia kompatybilnego z AC3.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_sysconfdir}}

install ffmpeg		$RPM_BUILD_ROOT%{_bindir}
install ffserver	$RPM_BUILD_ROOT%{_sbindir}
install doc/*.conf	$RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf README Change* doc/{bench.txt,ffmpeg.txt,ffserver.txt,README*,TODO}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(740,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*.conf
