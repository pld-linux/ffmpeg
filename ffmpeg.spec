# TODO
# - libnut enabled   no (http://www.nut-container.org/)
#
# Conditional build:
%bcond_with	amr		# build 3GPP Adaptive Multi Rate (AMR) speech codec
%bcond_without	autoreqdep	# don't care about package name deps generated by rpm
%bcond_without	imlib2		# don't build imlib2 vhook module
#
%define		_snap	2007-06-26
%define		snap	%(echo %{_snap} | tr -d -)
%define		_rel 2
Summary:	Realtime audio/video encoder and streaming server
Summary(pl.UTF-8):	Koder audio/wideo czasu rzeczywistego oraz serwer strumieni
Name:		ffmpeg
Version:	0.4.9
Release:	3.%{snap}.%{_rel}
# LGPL or GPL, chosen at configure time (GPL version is more featured)
# (postprocessing, a52, xvid, x264, faad)
License:	GPL with LGPL parts
Group:		Applications/Multimedia
#Source0:	http://dl.sourceforge.net/ffmpeg/%{name}-%{version}-pre1.tar.gz
Source0:	http://ffmpeg.mplayerhq.hu/%{name}-export-snapshot.tar.bz2
# Source0-md5:	94409403b09bc5e1b26c9853188778ae
Source1:	ffserver.init
Source2:	ffserver.sysconfig
Source3:	ffserver.conf
Patch0:		%{name}-gcc4.patch
Patch1:		%{name}-img_convert_symbol.patch
Patch2:		%{name}-fork.patch
URL:		http://ffmpeg.mplayerhq.hu/
BuildRequires:	SDL-devel
BuildRequires:	a52dec-libs-devel
%if %{with amr}
BuildRequires:	amrnb-devel >= 6.1.0.4
BuildRequires:	amrwb-devel >= 7.0.0.1
%endif
BuildRequires:	faac-devel
BuildRequires:	faad2-devel
BuildRequires:	freetype-devel
%ifarch ppc
# require version with altivec support fixed
BuildRequires:	gcc >= 5:3.3.2-3
%endif
%{?with_imlib2:BuildRequires:	imlib2-devel >= 1.3.0}
BuildRequires:	lame-libs-devel
BuildRequires:	libgsm-devel
BuildRequires:	libogg-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libtheora-devel >= 1.0-0.alpha7
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	libvorbis-devel
BuildRequires:	libx264-devel >= 0.1.2-1.20061024_2245.1
%ifarch %{ix86}
%ifnarch i386 i486
BuildRequires:	nasm
%endif
%endif
BuildRequires:	perl-tools-pod
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	tetex
BuildRequires:	texinfo
%{?with_amr:BuildRequires:	unzip}
BuildRequires:	xvid-devel >= 1:1.1.0
BuildRequires:	zlib-devel
%{?with_autoreqdep:BuildConflicts:	libpostproc}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	xvid >= 1:1.1.0
Obsoletes:	libpostproc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%define		specflags	-fno-strict-aliasing

# -fomit-frame-pointer is always needed on x86 due to lack of registers (-fPIC takes one)
%define		specflags_ia32	-fomit-frame-pointer
# -mmmx is needed to enable <mmintrin.h> code.
%define		specflags_i586	-mmmx
%define		specflags_i686	-mmmx

%description
ffmpeg is a hyper fast realtime audio/video encoder and streaming
server. It can grab from a standard Video4Linux video source and
convert it into several file formats based on DCT/motion compensation
encoding. Sound is compressed in MPEG audio layer 2 or using an AC3
compatible stream.

%description -l pl.UTF-8
ffmpeg jest bardzo szybkim koderem audio/wideo w czasie rzeczywistym
oraz serwerem strumieni multimedialnych. ffmpeg potrafi zrzucać dane
ze standardowego urządzenia Video4Linux i przekonwertować je w kilka
formatów plików bazujących na kodowaniu DCT/kompensacji ruchu. Dźwięk
jest kompresowany do strumienia MPEG audio layer 2 lub używając
strumienia kompatybilnego z AC3.

%package libs
Summary:	ffmpeg libraries
Summary(pl.UTF-8):	Biblioteki ffmpeg
Group:		Libraries

%description libs
This package contains ffmpeg shared libraries.

%description libs -l pl.UTF-8
Ten pakiet zawiera biblioteki współdzielone ffmpeg.

%package devel
Summary:	ffmpeg header files
Summary(pl.UTF-8):	Pliki nagłówkowe ffmpeg
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
# for libavcodec:
%if %{with amr}
Requires:	amrnb-devel
Requires:	amrwb-devel >= 5.3.0
%endif
Requires:	faac-devel
Requires:	faad2-devel
Requires:	lame-libs-devel
Requires:	libgsm-devel
Requires:	libtheora-devel >= 1.0-0.alpha7
Requires:	libvorbis-devel
Requires:	libx264-devel >= 0.1.2-1.20060828_2245.1
Requires:	xvid-devel >= 1:1.1.0
Requires:	zlib-devel
Obsoletes:	libpostproc-devel

%description devel
ffmpeg header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe ffmpeg.

%package static
Summary:	ffmpeg static libraries
Summary(pl.UTF-8):	Statyczne biblioteki ffmpeg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
ffmpeg static libraries (libavcodec and libavformat).

%description static -l pl.UTF-8
Statyczne biblioteki ffmpeg (libavcodec i libavformat).

%package ffplay
Summary:	FFplay - SDL-based media player
Summary(pl.UTF-8):	FFplay - odtwarzacz mediów oparty na SDL
Group:		Applications/Multimedia
Requires:	%{name}-libs = %{version}-%{release}

%description ffplay
FFplay is a very simple and portable media player using the FFmpeg
libraries and the SDL library. It is mostly used as a test bench for
the various APIs of FFmpeg.

%description ffplay -l pl.UTF-8
FFplay to bardzo prosty i przenośny odtwarzacz mediów używający
bibliotek FFmpeg oraz biblioteki SDL. Jest używany głównie do
testowania różnych API FFmpeg.

%package vhook-imlib2
Summary:	imlib2 based hook
Summary(pl.UTF-8):	Moduł przejściowy oparty o imlib2
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description vhook-imlib2
This module implements a text overlay for a video image. Currently it
supports a fixed overlay or reading the text from a file. The string
is passed through strftime so that it is easy to imprint the date and
time onto the image.

%description vhook-imlib2 -l pl.UTF-8
Ten moduł implementuje tekstową nakładkę dla obrazu. Aktualnie
obsługuje stałą nakładkę lub wczytywanie tekstu z pliku. Łańcuch jest
przepuszczany przez strftime, więc łatwo umieścić datę i czas na
obrazie.

%package ffserver
Summary:	FFserver video server
Summary(pl.UTF-8):	FFserver - serwer strumieni obrazu
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires:	rc-scripts >= 0.4.0.10

%description ffserver
FFserver is a streaming server for both audio and video. It supports
several live feeds, streaming from files and time shifting on live
feeds (you can seek to positions in the past on each live feed,
provided you specify a big enough feed storage in ffserver.conf).

%description ffserver -l pl.UTF-8
FFserver to serwer strumieni dla dźwięku i obrazu. Obsługuje kilka
źródeł na żywo, przekazywanie strumieni z plików i przesuwanie w
czasie dla źródeł na żywo (można przeskakiwać na położenia w
przeszłości dla każdego źródła na żywo, pod warunkiem odpowiednio
dużej przestrzeni na dane skonfigurowanej w ffserver.conf).

%prep
%setup -q -n %{name}-export-%{_snap}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# notes:
# - it's not autoconf configure
# - --disable-debug, --disable-opts, tune=generic causes not to override our optflags
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--shlibdir=%{_libdir} \
	--mandir=%{_mandir} \
	--disable-strip \
	--enable-liba52 \
	--enable-liba52bin \
	--enable-libfaac \
	--enable-libfaad \
	--enable-libfaadbin \
	--enable-gpl \
	--enable-libgsm \
	--enable-libogg \
	--enable-libtheora \
	--enable-libmp3lame \
	--enable-pp \
	--enable-pthreads \
	--enable-shared \
	--enable-swscaler \
	--enable-libvorbis \
	--enable-libx264 \
	--enable-libxvid \
%ifnarch %{ix86} %{x8664}
	--disable-mmx \
%endif
%ifarch i386 i486
	--disable-mmx \
%endif
%if %{with amr}
	--enable-libamr-nb \
	--enable-libamr-wb \
%endif
	--cc="%{__cc}" \
	--extra-cflags="%{rpmcflags}" \
	--extra-ldflags="%{rpmldflags}" \
	--disable-debug \
	--disable-opts \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},/etc/{sysconfig,rc.d/init.d}} \
	$RPM_BUILD_ROOT/var/{cache,log}/ffserver

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install config.h $RPM_BUILD_ROOT%{_includedir}/ffmpeg
install libavformat/allformats.h $RPM_BUILD_ROOT%{_includedir}/ffmpeg
install libavutil/intreadwrite.h $RPM_BUILD_ROOT%{_includedir}/ffmpeg
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ffserver
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/ffserver
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/ffserver.conf
mv -f $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}/ffserver

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%pre ffserver
%groupadd -g 167 ffserver
%useradd -g ffserver -u 167 ffserver

%post ffserver
/sbin/chkconfig --add ffserver
%service ffserver restart

%preun ffserver
if [ "$1" = 0 ]; then
	%service ffserver stop
	/sbin/chkconfig --del ffserver
fi

%postun ffserver
if [ "$1" = 0 ]; then
	%userremove ffserver
	%groupremove ffserver
fi

%files
%defattr(644,root,root,755)
%doc Changelog README doc/*.html doc/TODO
%attr(755,root,root) %{_bindir}/ffmpeg
%{_mandir}/man1/ffmpeg.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavcodec.so.*.*.*
%attr(755,root,root) %{_libdir}/libavformat.so.*.*.*
%attr(755,root,root) %{_libdir}/libavutil.so.*.*.*
%attr(755,root,root) %{_libdir}/libpostproc.so.*.*.*
%attr(755,root,root) %{_libdir}/libswscale.so.*.*.*
%dir %{_libdir}/vhook
%attr(755,root,root) %{_libdir}/vhook/drawtext.so
%attr(755,root,root) %{_libdir}/vhook/fish.so
%attr(755,root,root) %{_libdir}/vhook/null.so
%attr(755,root,root) %{_libdir}/vhook/ppm.so
%attr(755,root,root) %{_libdir}/vhook/watermark.so

%files devel
%defattr(644,root,root,755)
%doc doc/optimization.txt
%attr(755,root,root) %{_libdir}/libavcodec.so
%attr(755,root,root) %{_libdir}/libavformat.so
%attr(755,root,root) %{_libdir}/libavutil.so
%attr(755,root,root) %{_libdir}/libpostproc.so
%attr(755,root,root) %{_libdir}/libswscale.so
%{_includedir}/ffmpeg
%{_includedir}/postproc
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files ffplay
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ffplay
%{_mandir}/man1/ffplay.1*

%if %{with imlib2}
%files vhook-imlib2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vhook/imlib2.so
%endif

%files ffserver
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ffserver.conf
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/ffserver
%attr(755,root,root) %{_sbindir}/ffserver
%attr(754,root,root) /etc/rc.d/init.d/ffserver
%{_mandir}/man1/ffserver.1*
%dir %attr(770,root,ffserver) /var/cache/ffserver
%dir %attr(770,root,ffserver) /var/log/ffserver
