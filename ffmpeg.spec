#
# How to deal with ffmpeg/opencv checken-egg problem:
#	1. make-request -r --without opencv ffmpeg.spec
#	2. make-request -r opencv.spec
#	3. bump release of ffmpeg.spec
#	4. make-request -r ffmpeg.spec
#
# Conditional build:
%bcond_with	nonfree		# non free options of package (currently: faac)
%bcond_with	aacplus		# AAC+ encoding via libaacplus (requires nonfree)
%bcond_with	fdk_aac		# AAC encoding via libfdk_aac (requires nonfree)
%bcond_without	caca		# textual display using libcaca
%bcond_without	flite		# flite voice synthesis support
%bcond_without	frei0r		# frei0r video filtering
%bcond_without	ilbc		# iLBC de/encoding via WebRTC libilbc
%bcond_without	openal		# OpenAL 1.1 capture support
%bcond_without	opencv		# OpenCV video filtering
%bcond_without	pulseaudio	# PulseAudio input support
%bcond_without	soxr		# SoX Resampler support
%bcond_without	x264		# x264 encoder
%bcond_without	utvideo		# Ut Video decoder
%bcond_without	va		# VAAPI (Video Acceleration API)
%bcond_without	vpx		# VP8, a high-quality video codec
%bcond_without	doc		# don't build docs

Summary:	FFmpeg - a very fast video and audio converter
Summary(pl.UTF-8):	FFmpeg - szybki konwerter audio/wideo
Name:		ffmpeg
Version:	1.1
Release:	1
# LGPL or GPL, chosen at configure time (GPL version is more featured)
# (postprocessing, some filters, x264, xavs, xvid, x11grab)
# using v3 allows Apache-licensed libs (opencore-amr, libvo-*enc)
License:	GPL v3+ with LGPL v3+ parts
Group:		Applications/Multimedia
Source0:	http://ffmpeg.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	578c590a0e996c1fc71acb666c0ed858
Source1:	ffserver.init
Source2:	ffserver.sysconfig
Source3:	ffserver.conf
Patch0:		%{name}-gsm.patch
Patch1:		%{name}-opencv24.patch
Patch2:		%{name}-cdio-paranoia.patch
Patch3:		%{name}-utvideo.patch
URL:		http://www.ffmpeg.org/
%{?with_openal:BuildRequires:	OpenAL-devel >= 1.1}
BuildRequires:	SDL-devel >= 1.2.1
BuildRequires:	alsa-lib-devel
BuildRequires:	bzip2-devel
BuildRequires:	celt-devel >= 0.11.0
%{?with_nonfree:BuildRequires:	faac-devel}
%{?with_fdk_aac:BuildRequires:	fdk-aac-devel}
%{?with_flite:BuildRequires:	flite-devel >= 1.4}
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
%{?with_frei0r:BuildRequires:	frei0r-devel}
%ifarch ppc
# require version with altivec support fixed
BuildRequires:	gcc >= 5:3.3.2-3
%endif
BuildRequires:	gnutls-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lame-libs-devel >= 3.98.3
%{?with_aacplus:BuildRequires:	libaacplus-devel >= 2.0.0}
BuildRequires:	libass-devel
BuildRequires:	libavc1394-devel
BuildRequires:	libbluray-devel
%{?with_caca:BuildRequires:	libcaca-devel}
BuildRequires:	libcdio-paranoia-devel >= 0.90-2
BuildRequires:	libdc1394-devel >= 2
BuildRequires:	libgsm-devel
BuildRequires:	libiec61883-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libnut-devel
BuildRequires:	libraw1394-devel >= 2
BuildRequires:	librtmp-devel
BuildRequires:	libtheora-devel >= 1.0-0.beta3
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	libv4l-devel
%{?with_va:BuildRequires:	libva-devel >= 1.0.3}
BuildRequires:	libvdpau-devel >= 0.2
BuildRequires:	libvorbis-devel
%{?with_vpx:BuildRequires:	libvpx-devel >= 0.9.7}
# X264_BUILD >= 118
%{?with_x264:BuildRequires:	libx264-devel >= 0.1.3-1.20111212_2245}
%ifarch %{ix86}
%ifnarch i386 i486
BuildRequires:	nasm
%endif
%endif
BuildRequires:	opencore-amr-devel
%{?with_opencv:BuildRequires:	opencv-devel}
BuildRequires:	openjpeg-devel >= 1.5
BuildRequires:	opus-devel
BuildRequires:	perl-Encode
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel}
BuildRequires:	rpmbuild(macros) >= 1.470
BuildRequires:	schroedinger-devel
%{?with_soxr:BuildRequires:	soxr-devel}
BuildRequires:	speex-devel >= 1:1.2-rc1
%{?with_doc:BuildRequires:	tetex}
%{?with_doc:BuildRequires:	texi2html}
%{?with_doc:BuildRequires:	texinfo}
BuildRequires:	twolame-devel
%{?with_utvideo:BuildRequires:	utvideo-devel >= 12}
BuildRequires:	vo-aacenc-devel
BuildRequires:	vo-amrwbenc-devel
%{?with_ilbc:BuildRequires:	webrtc-libilbc-devel}
BuildRequires:	xavs-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xvid-devel >= 1:1.1.0
BuildRequires:	yasm
BuildRequires:	zlib-devel
%{?with_autoreqdep:BuildConflicts:	libpostproc}
# overflows maximum hash table size
BuildConflicts:	pdksh < 5.2.14-57
Requires:	%{name}-libs = %{version}-%{release}
%{?with_utvideo:Requires:	utvideo >= 12}
%{?with_ilbc:Requires:	webrtc-libilbc}
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
%define		specflags_ppc	-fPIC

%description
FFmpeg is a complete solution to record, convert and stream audio and
video. It is a command line tool to convert one video file format to
another. It also supports grabbing and encoding in real time from a TV
card.

%description -l pl.UTF-8
FFmpeg to kompletne rozwiązanie nagrywania, konwersji i transmisji
strumieni dźwięku i obrazu. Jest to działające z linii poleceń
narzędzie do konwersji obrazu z jednego formatu do innego. Obsługuje
także przechwytywanie i kodowanie w czasie rzeczywistym z karty
telewizyjnej.

%package libs
Summary:	ffmpeg libraries
Summary(pl.UTF-8):	Biblioteki ffmpeg
Group:		Libraries

%description libs
This package contains the ffmpeg shared libraries:
- the codec library (libavcodec). It supports most existing encoding
  formats (MPEG, DivX, MPEG4, AC3, DV...),
- demuxer library (libavformat). It supports most existing file
  formats (AVI, MPEG, OGG, Matroska, ASF...),
- video postprocessing library (libpostproc).

%description libs -l pl.UTF-8
Ten pakiet zawiera biblioteki współdzielone ffmpeg:
- bibliotekę kodeków (libavcodec); obsługuje większość istniejących
  formatów kodowania (MPEG, DivX, MPEG4, AC3, DV...),
- bibliotekę demuksera (libavformat); obsługuje większość istniejących
  formatów plików (AVI, MPEG, OGG, Matroska, ASF...),
- bibliotekę postprocessingu (libpostproc).

%package devel
Summary:	ffmpeg header files
Summary(pl.UTF-8):	Pliki nagłówkowe ffmpeg
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
# Libs.private from *.pc (unreasonably they are all the same)
Requires:	SDL-devel >= 1.2.1
Requires:	alsa-lib-devel
Requires:	bzip2-devel
Requires:	celt-devel >= 0.11.0
%{?with_nonfree:Requires:	faac-devel}
%{?with_fdk_aac:Requires:	fdk-aac-devel}
Requires:	fontconfig-devel
Requires:	freetype-devel
Requires:	jack-audio-connection-kit-devel
%{?with_flite:Requires:	flite-devel >= 1.4}
Requires:	lame-libs-devel >= 3.98.3
%{?with_aacplus:Requires:	libaacplus-devel >= 2.0.0}
Requires:	libass-devel
Requires:	libavc1394-devel
Requires:	libbluray-devel
%{?with_caca:Requires:	libcaca-devel}
Requires:	libcdio-paranoia-devel >= 0.90-2
Requires:	libdc1394-devel >= 2
Requires:	libgsm-devel
Requires:	libiec61883-devel
Requires:	libmodplug-devel
Requires:	libnut-devel
Requires:	libraw1394-devel >= 2
Requires:	librtmp-devel
Requires:	libtheora-devel >= 1.0-0.beta3
%{?with_va:Requires:	libva-devel >= 1.0.3}
Requires:	libvorbis-devel
%{?with_vpx:Requires:	libvpx-devel >= 0.9.7}
%{?with_x264:Requires:	libx264-devel >= 0.1.3-1.20110625_2245}
Requires:	opencore-amr-devel
%{?with_opencv:Requires:	opencv-devel}
Requires:	openjpeg-devel >= 1.5
Requires:	schroedinger-devel
%{?with_soxr:Requires:	soxr-devel}
Requires:	speex-devel >= 1:1.2-rc1
Requires:	twolame-devel
%{?with_utvideo:Requires:	utvideo-devel >= 12}
Requires:	vo-aacenc-devel
Requires:	vo-amrwbenc-devel
%{?with_ilbc:Requires:	webrtc-libilbc-devel}
Requires:	xavs-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel
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
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# package the grep result for mplayer, the result formatted as ./mplayer/configure
cat <<EOF > ffmpeg-avconfig
#! /bin/sh
_libavdecoders_all="`sed -n 's/^[^#]*DEC.*(.*, *\(.*\)).*/\1_decoder/p' libavcodec/allcodecs.c | tr '[a-z]' '[A-Z]'`"
_libavencoders_all="`sed -n 's/^[^#]*ENC.*(.*, *\(.*\)).*/\1_encoder/p' libavcodec/allcodecs.c | tr '[a-z]' '[A-Z]'`"
_libavparsers_all="`sed -n 's/^[^#]*PARSER.*(.*, *\(.*\)).*/\1_parser/p' libavcodec/allcodecs.c | tr '[a-z]' '[A-Z]'`"
_libavbsfs_all="`sed -n 's/^[^#]*BSF.*(.*, *\(.*\)).*/\1_bsf/p' libavcodec/allcodecs.c | tr '[a-z]' '[A-Z]'`"
_libavdemuxers_all="`sed -n 's/^[^#]*DEMUX.*(.*, *\(.*\)).*/\1_demuxer/p' libavformat/allformats.c | tr '[a-z]' '[A-Z]'`"
_libavmuxers_all="`sed -n 's/^[^#]*_MUX.*(.*, *\(.*\)).*/\1_muxer/p' libavformat/allformats.c | tr '[a-z]' '[A-Z]'`"
_libavprotocols_all="`sed -n 's/^[^#]*PROTOCOL.*(.*, *\(.*\)).*/\1_protocol/p' libavformat/allformats.c | tr '[a-z]' '[A-Z]'`"
EOF
cat <<'EOF' >> ffmpeg-avconfig

case "$1" in
--decoders)
	echo $_libavdecoders_all
	;;
--encoders)
	echo $_libavencoders_all
	;;
--parsers)
	echo $_libavparsers_all
	;;
--bsfs)
	echo $_libavbsfs_all
	;;
--demuxers)
	echo $_libavdemuxers_all
	;;
--muxers)
	echo $_libavmuxers_all
	;;
--protocols)
	echo $_libavprotocols_all
	;;
*)
	cat <<USAGE
Usage: $0 [OPTION]
Options:
  --decoders
  --encoders
  --parsers
  --bsfs
  --demuxers
  --muxers
  --protocols
USAGE
	exit 1;;
esac

exit 0
EOF

%build
# notes:
# - it's not autoconf configure
# - --disable-debug, --disable-optimizations, tune=generic causes not to override our optflags
./configure \
	--arch=%{_target_base_arch} \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--shlibdir=%{_libdir} \
	--mandir=%{_mandir} \
	--extra-cflags="-D_GNU_SOURCE=1 %{rpmcppflags} %{rpmcflags}" \
	--extra-ldflags="%{rpmcflags} %{rpmldflags}" \
	--cc="%{__cc}" \
	--disable-debug \
	--disable-optimizations \
	--disable-stripping \
	--enable-avfilter \
	--enable-avresample \
	--enable-gnutls \
	--enable-gpl \
	--enable-version3 \
	--enable-fontconfig \
	%{?with_frei0r:--enable-frei0r} \
	%{?with_aacplus:--enable-libaacplus} \
	--enable-libass \
	--enable-libbluray \
	%{?with_caca:--enable-libcaca} \
	--enable-libcelt \
	--enable-libcdio \
	--enable-libdc1394 \
	%{?with_fdk_aac:--enable-libfdk-aac} \
	%{?with_flite:--enable-libflite} \
	--enable-libfreetype \
	--enable-libgsm \
	--enable-libiec61883 \
	%{?with_ilbc:--enable-libilbc} \
	--enable-libmodplug \
	--enable-libmp3lame \
	--enable-libnut \
	--enable-libopencore-amrnb \
	--enable-libopencore-amrwb \
	%{?with_opencv:--enable-libopencv} \
	--enable-libopenjpeg \
	--enable-libopus \
	%{?with_pulseaudio:--enable-libpulse} \
	--enable-librtmp \
	--enable-libschroedinger \
	%{?with_soxr:--enable-libsoxr} \
	--enable-libspeex \
	--enable-libtheora \
	--enable-libtwolame \
	%{?with_utvideo:--enable-libutvideo} \
	--enable-libv4l2 \
	--enable-libvo-aacenc \
	--enable-libvo-amrwbenc \
	--enable-libvorbis \
	%{?with_vpx:--enable-libvpx} \
	%{?with_x264:--enable-libx264} \
	--enable-libxavs \
	--enable-libxvid \
	%{?with_openal:--enable-openal} \
	--enable-postproc \
	--enable-pthreads \
	--enable-shared \
	--enable-swscale \
	%{?with_va:--enable-vaapi} \
	--enable-vdpau \
	--enable-x11grab \
%ifnarch %{ix86} %{x8664}
	--disable-mmx \
%endif
%ifarch i386 i486
	--disable-mmx \
%endif
%if %{with nonfree}
	--enable-nonfree \
	--enable-libfaac \
%endif
	--enable-runtime-cpudetect

# force oldscaler build
%{__sed} -i -e 's|#define.*CONFIG_OLDSCALER.*0|#define CONFIG_OLDSCALER 1|g' config.h

%{__make} \
	V=1

# CC_O to add -c to commandline. makefile should be patched
%{__make} tools/qt-faststart V=1 CC_O='-c -o $@'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},/etc/{sysconfig,rc.d/init.d}} \
	$RPM_BUILD_ROOT%{_includedir}/ffmpeg \
	$RPM_BUILD_ROOT/var/{cache,log}/ffserver

%{__make} install install-headers \
	DESTDIR=$RPM_BUILD_ROOT \
	V=1

# install nonstandard, non-public headers manually
cp -a config.h $RPM_BUILD_ROOT%{_includedir}/ffmpeg
for a in libavutil/*/bswap.h; do
	install -Dp $a $RPM_BUILD_ROOT%{_includedir}/$a
done
cp -a libavformat/riff.h $RPM_BUILD_ROOT%{_includedir}/libavformat
# for lim-omx ffmpeg components
cp -a libavcodec/audioconvert.h $RPM_BUILD_ROOT%{_includedir}/libavcodec

install -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ffserver
cp -a %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/ffserver
cp -a %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/ffserver.conf
mv -f $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}/ffserver
install -p tools/qt-faststart $RPM_BUILD_ROOT%{_bindir}

# install as ffmpeg-avconfig to avoid with possible programs looking for
# ffmpeg-config and expecting --libs output from it which is not implemented
# simple to do (by querying pkgconfig), but why?
install -p ffmpeg-avconfig $RPM_BUILD_ROOT%{_bindir}/ffmpeg-avconfig

# fix man page
%if %{with doc}
install -d $RPM_BUILD_ROOT%{_mandir}/man3
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/lib*.3 $RPM_BUILD_ROOT%{_mandir}/man3
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

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
%doc CREDITS LICENSE MAINTAINERS README doc/{APIchanges,RELEASE_NOTES} %{?with_doc:doc/*.html}
%attr(755,root,root) %{_bindir}/ffmpeg
%attr(755,root,root) %{_bindir}/ffprobe
%attr(755,root,root) %{_bindir}/qt-faststart
%dir %{_datadir}/ffmpeg
%{_datadir}/ffmpeg/*.ffpreset
%{_datadir}/ffmpeg/ffprobe.xsd
%if %{with doc}
%{_mandir}/man1/ffmpeg.1*
%{_mandir}/man1/ffmpeg-bitstream-filters.1*
%{_mandir}/man1/ffmpeg-codecs.1*
%{_mandir}/man1/ffmpeg-devices.1*
%{_mandir}/man1/ffmpeg-filters.1*
%{_mandir}/man1/ffmpeg-formats.1*
%{_mandir}/man1/ffmpeg-protocols.1*
%{_mandir}/man1/ffmpeg-resampler.1*
%{_mandir}/man1/ffmpeg-scaler.1*
%{_mandir}/man1/ffmpeg-utils.1*
%{_mandir}/man1/ffprobe.1*
%endif

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavcodec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavcodec.so.54
%attr(755,root,root) %{_libdir}/libavdevice.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavdevice.so.54
%attr(755,root,root) %{_libdir}/libavfilter.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavfilter.so.3
%attr(755,root,root) %{_libdir}/libavformat.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavformat.so.54
%attr(755,root,root) %{_libdir}/libavresample.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavresample.so.1
%attr(755,root,root) %{_libdir}/libavutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavutil.so.52
%attr(755,root,root) %{_libdir}/libpostproc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpostproc.so.52
%attr(755,root,root) %{_libdir}/libswresample.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libswresample.so.0
%attr(755,root,root) %{_libdir}/libswscale.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libswscale.so.2

%files devel
%defattr(644,root,root,755)
%doc doc/optimization.txt
%attr(755,root,root) %{_bindir}/ffmpeg-avconfig
%attr(755,root,root) %{_libdir}/libavcodec.so
%attr(755,root,root) %{_libdir}/libavdevice.so
%attr(755,root,root) %{_libdir}/libavfilter.so
%attr(755,root,root) %{_libdir}/libavformat.so
%attr(755,root,root) %{_libdir}/libavresample.so
%attr(755,root,root) %{_libdir}/libavutil.so
%attr(755,root,root) %{_libdir}/libpostproc.so
%attr(755,root,root) %{_libdir}/libswresample.so
%attr(755,root,root) %{_libdir}/libswscale.so
%{_includedir}/ffmpeg
%{_includedir}/libavcodec
%{_includedir}/libavdevice
%{_includedir}/libavfilter
%{_includedir}/libavformat
%{_includedir}/libavresample
%{_includedir}/libavutil
%{_includedir}/libpostproc
%{_includedir}/libswresample
%{_includedir}/libswscale
%{_pkgconfigdir}/libavcodec.pc
%{_pkgconfigdir}/libavdevice.pc
%{_pkgconfigdir}/libavfilter.pc
%{_pkgconfigdir}/libavformat.pc
%{_pkgconfigdir}/libavresample.pc
%{_pkgconfigdir}/libavutil.pc
%{_pkgconfigdir}/libpostproc.pc
%{_pkgconfigdir}/libswresample.pc
%{_pkgconfigdir}/libswscale.pc
%if %{with doc}
%{_mandir}/man3/libavcodec.3*
%{_mandir}/man3/libavdevice.3*
%{_mandir}/man3/libavfilter.3*
%{_mandir}/man3/libavformat.3*
%{_mandir}/man3/libavutil.3*
%{_mandir}/man3/libswresample.3*
%{_mandir}/man3/libswscale.3*
%endif

%files static
%defattr(644,root,root,755)
%{_libdir}/libavcodec.a
%{_libdir}/libavdevice.a
%{_libdir}/libavfilter.a
%{_libdir}/libavformat.a
%{_libdir}/libavresample.a
%{_libdir}/libavutil.a
%{_libdir}/libpostproc.a
%{_libdir}/libswresample.a
%{_libdir}/libswscale.a

%files ffplay
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ffplay
%{?with_doc:%{_mandir}/man1/ffplay.1*}

%files ffserver
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ffserver.conf
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/ffserver
%attr(755,root,root) %{_sbindir}/ffserver
%attr(754,root,root) /etc/rc.d/init.d/ffserver
%{?with_doc:%{_mandir}/man1/ffserver.1*}
%dir %attr(770,root,ffserver) /var/cache/ffserver
%dir %attr(770,root,ffserver) /var/log/ffserver
