#
# TODO: update for lzo 2.x (currently only lzo 1.x is supported)
#
# Conditional build:
%bcond_without	amr		# don't build 3GPP Adaptive Multi Rate (AMR) speech codec
%bcond_without	autoreqdep	# don't care about package name deps generated by rpm
%bcond_without	imlib2		# don't build imlib2 vhook module
%bcond_with	lzo		# build with LZO support
#
Summary:	Realtime audio/video encoder and streaming server
Summary(pl):	Koder audio/wideo czasu rzeczywistego oraz serwer strumieni
Name:		ffmpeg
Version:	0.4.9
%define		snap	20060129
%define		_rel 12
Release:	3.%{snap}.%{_rel}
# LGPL or GPL, chosen at configure time (GPL version is more featured)
# (postprocessing, a52, xvid, x264, dts, faad)
License:	GPL with LGPL parts
Group:		Applications/Multimedia
#Source0:	http://dl.sourceforge.net/ffmpeg/%{name}-%{version}-pre1.tar.gz
#Source0:	ftp://ftp2.mplayerhq.hu/MPlayer/cvs/FFMpeg-%{snap}.tar.bz2
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	d8ea09431d6c0c91bfd35e0ca74a67e1
Source1:	ffserver.init
Source2:	ffserver.sysconfig
Source3:	ffserver.conf
Patch0:		%{name}-libtool.patch
Patch1:		%{name}-libdir.patch
Patch2:		%{name}-gcc4.patch
Patch3:		%{name}-system-amr.patch
URL:		http://ffmpeg.mplayerhq.hu/
BuildRequires:	SDL-devel
%if %{with amr}
BuildRequires:	amrnb-devel
BuildRequires:	amrwb-devel >= 5.3.0
%endif
BuildRequires:	faac-devel
BuildRequires:	faad2-devel
BuildRequires:	freetype-devel
%ifarch ppc
# require version with altivec support fixed
BuildRequires:	gcc >= 5:3.3.2-3
%endif
%{?with_imlib2:BuildRequires:	imlib2-devel >= 1.1.0-2}
BuildRequires:	lame-libs-devel
BuildRequires:	libdts-devel
BuildRequires:	libgsm-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	libvorbis-devel
BuildRequires:	libx264-devel >= 0.1.2-1.20060430_2245.1
%{?with_lzo:BuildRequires:	lzo-devel < 2.0}
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

%description -l pl
ffmpeg jest bardzo szybkim koderem audio/wideo w czasie rzeczywistym
oraz serwerem strumieni multimedialnych. ffmpeg potrafi zrzuca� dane
ze standardowego urz�dzenia Video4Linux i przekonwertowa� je w kilka
format�w plik�w bazuj�cych na kodowaniu DCT/kompensacji ruchu. D�wi�k
jest kompresowany do strumienia MPEG audio layer 2 lub u�ywaj�c
strumienia kompatybilnego z AC3.

%package libs
Summary:	ffmpeg libraries
Summary(pl):	Biblioteki ffmpeg
Group:		Libraries

%description libs
This package contains ffmpeg shared libraries.

%description libs -l pl
Ten pakiet zawiera biblioteki wsp�dzielone ffmpeg.

%package devel
Summary:	ffmpeg header files
Summary(pl):	Pliki nag��wkowe ffmpeg
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
Requires:	libdts-devel
Requires:	libgsm-devel
Requires:	libtheora-devel
Requires:	libvorbis-devel
%{?with_lzo:Requires:	lzo-devel < 2.0}
Requires:	libx264-devel >= 0.1.2-1.20060430_2245.1
Requires:	xvid-devel >= 1:1.1.0
Requires:	zlib-devel
Obsoletes:	libpostproc-devel

%description devel
ffmpeg header files.

%description devel -l pl
Pliki nag��wkowe ffmpeg.

%package static
Summary:	ffmpeg static libraries
Summary(pl):	Statyczne biblioteki ffmpeg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
ffmpeg static libraries (libavcodec and libavformat).

%description static -l pl
Statyczne biblioteki ffmpeg (libavcodec i libavformat).

%package ffplay
Summary:	FFplay - SDL-based media player
Summary(pl):	FFplay - odtwarzacz medi�w oparty na SDL
Group:		Applications/Multimedia
Requires:	%{name}-libs = %{version}-%{release}

%description ffplay
FFplay is a very simple and portable media player using the FFmpeg
libraries and the SDL library. It is mostly used as a test bench for
the various APIs of FFmpeg.

%description ffplay -l pl
FFplay to bardzo prosty i przeno�ny odtwarzacz medi�w u�ywaj�cy
bibliotek FFmpeg oraz biblioteki SDL. Jest u�ywany g��wnie do
testowania r�nych API FFmpeg.

%package vhook-imlib2
Summary:	imlib2 based hook
Summary(pl):	Modu� przej�ciowy oparty o imlib2
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description vhook-imlib2
This module implements a text overlay for a video image. Currently it
supports a fixed overlay or reading the text from a file. The string
is passed through strftime so that it is easy to imprint the date and
time onto the image.

%description vhook-imlib2 -l pl
Ten modu� implementuje tekstow� nak�adk� dla obrazu. Aktualnie
obs�uguje sta�� nak�adk� lub wczytywanie tekstu z pliku. �a�cuch jest
przepuszczany przez strftime, wi�c �atwo umie�ci� dat� i czas na
obrazie.

%package ffserver
Summary:	FFserver video server
Summary(pl):	FFserver - serwer strumieni obrazu
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts >= 0.4.0.10
Requires:	%{name}-libs = %{version}-%{release}

%description ffserver
FFserver is a streaming server for both audio and video. It supports
several live feeds, streaming from files and time shifting on live
feeds (you can seek to positions in the past on each live feed,
provided you specify a big enough feed storage in ffserver.conf).

%description ffserver -l pl
FFserver to serwer strumieni dla d�wi�ku i obrazu. Obs�uguje kilka
�r�de� na �ywo, przekazywanie strumieni z plik�w i przesuwanie w
czasie dla �r�de� na �ywo (mo�na przeskakiwa� na po�o�enia w
przesz�o�ci dla ka�dego �r�d�a na �ywo, pod warunkiem odpowiednio
du�ej przestrzeni na dane skonfigurowanej w ffserver.conf).

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# notes:
# - it's not autoconf configure
# - --disable-debug, --disable-opts, tune=generic causes not to override our optflags
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	%{!?with_lzo:--disable-lzo} \
	--disable-strip \
	--enable-a52 \
	--enable-a52bin \
	--enable-dts \
	--enable-faac \
	--enable-faad \
	--enable-faadbin \
	--enable-gpl \
	--enable-libgsm \
	--enable-libogg \
	--enable-mp3lame \
	--enable-pp \
	--enable-pthreads \
	--enable-shared \
	--enable-theora \
	--enable-vorbis \
	--enable-x264 \
	--enable-xvid \
%ifnarch %{ix86} %{x8664}
	--disable-mmx \
%endif
%ifarch i386 i486
	--disable-mmx \
%endif
%if %{with amr}
	--enable-amr_nb \
	--enable-amr_wb \
%endif
	--cc="%{__cc}" \
	--extra-cflags="%{rpmcflags}" \
	--extra-ldflags="%{rpmldflags}" \
	--disable-debug \
	--disable-opts \
	--tune=generic

%{__make} \
	BUILD_DOC=yes

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},/etc/{sysconfig,rc.d/init.d}} \
	$RPM_BUILD_ROOT/var/{cache,log}/ffserver

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install xvmc_render.h $RPM_BUILD_ROOT%{_includedir}/ffmpeg
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ffserver
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/ffserver
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/ffserver.conf
mv -f $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}/ffserver

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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
%{_libdir}/lib*.la
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
