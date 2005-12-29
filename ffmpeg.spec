#
# Conditional build:
%bcond_without	imlib2		# we can safely play without it :-)
%bcond_without	autoreqdep	# don't care about package name deps generated by rpm
%bcond_with	gcc4		# disable long inline mmx assembly.
				# gcc4+ doesn't like hard register pressure and won't be fixed.
				# ffmpeg and other apps should be rewritten with <mmintrin.h>.
#
Summary:	Realtime audio/video encoder and streaming server
Summary(pl):	Koder audio/wideo czasu rzeczywistego oraz serwer strumieni
Name:		ffmpeg
Version:	0.4.9
%define	snap	20050806
Release:	3.%{snap}.4
# LGPL or GPL, chosen at configure time (GPL version is more featured)
License:	GPL
Group:		Daemons
#Source0:	http://dl.sourceforge.net/ffmpeg/%{name}-%{version}-pre1.tar.gz
Source0:	ftp://ftp2.mplayerhq.hu/MPlayer/cvs/FFMpeg-%{snap}.tar.bz2
# Source0-md5:	f5ea3dd877c5df5b60356053642cf542
Patch0:		%{name}-libtool.patch
Patch1:		%{name}-libdir.patch
URL:		http://ffmpeg.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	faac-devel
BuildRequires:	freetype-devel
%ifarch ppc
# require version with altivec support fixed
BuildRequires:	gcc >= 5:3.3.2-3
%endif
%{?with_imlib2:BuildRequires:	imlib2-devel >= 1.1.0-2}
BuildRequires:	lame-libs-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	libvorbis-devel
%ifarch %{ix86}
%ifnarch i386 i486
BuildRequires:	nasm
%endif
%endif
BuildRequires:	perl-tools-pod
BuildRequires:	tetex
BuildRequires:	texinfo
BuildRequires:	xvid-devel
BuildRequires:	zlib-devel
%{?with_autoreqdep:BuildConflicts:	libpostproc}
Obsoletes:	libpostproc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

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
oraz serwerem strumieni multimedialnych. ffmpeg potrafi zrzuca� dane
ze standardowego urz�dzenia Video4Linux i przekonwertowa� je w kilka
format�w plik�w bazuj�cych na kodowaniu DCT/kompensacji ruchu. D�wi�k
jest kompresowany do strumienia MPEG audio layer 2 lub u�ywaj�c
strumienia kompatybilnego z AC3.

Ten pakiet zawiera tak�e biblioteki wsp�dzielone ffmpeg (libavcodec i
libavformat).

%package devel
Summary:	ffmpeg header files
Summary(pl):	Pliki nag��wkowe ffmpeg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libpostproc-devel
# for libavcodec:
Requires:	faac-devel
Requires:	lame-libs-devel
Requires:	libtheora-devel
Requires:	libvorbis-devel
Requires:	xvid-devel
Requires:	zlib-devel

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
Requires:	%{name} = %{version}-%{release}

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
Requires:	%{name} = %{version}-%{release}

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

%prep
%setup -q -n FFMpeg-%{snap}
%patch0 -p1
%patch1 -p1

%build
# notes:
# - it's not autoconf configure
# - -fomit-frame-pointer is always needed on x86 due to lack of registers
#   (-fPIC takes one)
# - --disable-debug, --disable-opts, tune=generic causes not to override our optflags
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--disable-strip \
	--enable-a52 \
	--enable-faac \
	--enable-faadbin \
	--enable-gpl \
	--enable-libogg \
	--enable-mp3lame \
	--enable-pp \
	--enable-pthreads \
	--enable-shared \
	--enable-shared-pp \
	--enable-theora \
	--enable-vorbis \
	--enable-xvid \
%if %{without gcc4}
%ifnarch %{ix86}
	--disable-mmx \
%endif
%ifarch i386 i486
	--disable-mmx \
%endif
%else
	--disable-mmx \
%endif
	--cc="%{__cc}" \
	--extra-cflags="%{rpmcflags} -fomit-frame-pointer -fno-strict-aliasing" \
	--extra-ldflags="%{rpmldflags}" \
	--disable-debug \
	--disable-opts \
	--tune=generic

%{__make} \
	BUILD_DOC=yes \
	LIBVERSION=%{snap}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install xvmc_render.h $RPM_BUILD_ROOT%{_includedir}/ffmpeg

mv -f $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}/ffserver
install doc/*.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changelog README doc/*.html
%attr(755,root,root) %{_bindir}/ffmpeg
%attr(755,root,root) %{_sbindir}/ffserver
%attr(755,root,root) %{_libdir}/libavcodec-*.so
%attr(755,root,root) %{_libdir}/libavformat-*.so
%attr(755,root,root) %{_libdir}/libavutil-*.so
%attr(755,root,root) %{_libdir}/libpostproc.so.*.*.*
%dir %{_libdir}/vhook
%attr(755,root,root) %{_libdir}/vhook/drawtext.so
%attr(755,root,root) %{_libdir}/vhook/fish.so
%attr(755,root,root) %{_libdir}/vhook/null.so
%attr(755,root,root) %{_libdir}/vhook/ppm.so
%attr(755,root,root) %{_libdir}/vhook/watermark.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ffserver.conf
%{_mandir}/man1/ffmpeg.1*
%{_mandir}/man1/ffserver.1*

%files devel
%defattr(644,root,root,755)
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
