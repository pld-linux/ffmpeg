Summary:	Realtime audio/video encoder and streaming server
Summary(pl):	Koder audio/wideo czasu rzeczywistego oraz serwer strumieni
Name:		ffmpeg
Version:	0.4.6
Release:	1
License:	LGPL/GPL
Group:		Daemons
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/ffmpeg/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
Patch1:		%{name}-imlib2.patch
Patch2:		%{name}-libtool.patch
URL:		http://ffmpeg.sourceforge.net/
BuildRequires:	imlib2-devel
BuildRequires:	libtool >= 1:1.4.2-9
%ifarch i586 i686 athlon
BuildRequires:	nasm
%endif
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ffmpeg is a hyper fast realtime audio/video encoder and streaming
server. It can grab from a standard Video4Linux video source and
convert it into several file formats based on DCT/motion compensation
encoding. Sound is compressed in MPEG audio layer 2 or using an AC3
compatible stream.

This package contains also ffmpeg shared libraries (libavcodec and
libavformat).

%description -l pl
ffmpeg jest bardzo szybkim koderem audio/wideo w czasie rzeczywistym
oraz serwerem strumieni multimedialnych. ffmpeg potrafi zrzucaæ dane
ze standardowego urz±dzenia Video4Linux i przekonwertowaæ je w kilka
formatów plików bazuj±cych na kodowaniu DCT/kompensacji ruchu. D¼wiêk
jest kompresowany do strumienia MPEG audio layer 2 lub u¿ywaj±c
strumienia kompatybilnego z AC3.

Ten pakiet zawiera tak¿e biblioteki wspó³dzielone ffmpeg (libavcodec i
libavformat).

%package vhook-imlib2
Summary:	imlib2 based hook
Summary(pl):	Modu³ przej¶ciowy oparty o imlib2
Group:		Libraries
Requires:	%{name} = %{version}

%description vhook-imlib2
This module implements a text overlay for a video image. Currently it
supports a fixed overlay or reading the text from a file. The string
is passed through strftime so that it is easy to imprint the date and
time onto the image.

%description vhook-imlib2 -l pl
Ten modu³ implementuje tekstow± nak³adkê dla obrazu. Aktualnie
obs³uguje sta³± nak³adkê lub wczytywanie tekstu z pliku. £añcuch jest
przepuszczany przez strftime, wiêc ³atwo umie¶ciæ datê i czas na
obrazie.

%package devel
Summary:	ffmpeg header files
Summary(pl):	Pliki nag³ówkowe ffmpeg
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
ffmpeg header files.

%description devel -l pl
Pliki nag³ówkowe ffmpeg.

%package static
Summary:	ffmpeg static libraries
Summary(pl):	Statyczne biblioteki ffmpeg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
ffmpeg static libraries (libavcodec and libavformat).

%description static -l pl
Statyczne biblioteki ffmpeg (libavcodec i libavformat).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# note: it's not autoconf configure
./configure \
	--prefix=%{_prefix} \
	--enable-shared \
	--enable-a52bin \
%ifnarch i586 i686 athlon
	--disable-mmx
%endif

# note: -fomit-frame-pointer is always needed on x86 due to lack of registers
#       (-fPIC takes one)
%{__make} \
	OPT="%{rpmcflags} -fomit-frame-pointer -I/usr/X11R6/include" \
	LDOPT="%{rpmldflags} -L/usr/X11R6/lib"

%{__make} -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}/ffserver
install doc/*.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changelog README doc/*.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/libavcodec-*.so
%attr(755,root,root) %{_libdir}/libavformat-*.so
%dir %{_libdir}/vhook
%attr(755,root,root) %{_libdir}/vhook/null.so
%attr(755,root,root) %{_libdir}/vhook/fish.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*.conf

%files vhook-imlib2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vhook/imlib2.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavcodec.so
%attr(755,root,root) %{_libdir}/libavformat.so
%{_libdir}/lib*.la
%{_includedir}/ffmpeg

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
