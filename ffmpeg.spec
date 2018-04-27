# TODO:
# - libvmaf [BR: libvmaf.pc, libvmaf, libvmaf.h]
# - libndi_newtek[nonfree, BR: Processing.NDI.Lib.h]
# - libmysofa [BR: libmysofa, mysofa.h]
# - rkmpp[GPLv3, BR: rockchip_mpp.pc, rockchip/rk_mpi_cmd.h, libdrm]
#
# How to deal with ffmpeg/opencv/chromaprint checken-egg problem:
#	1. make-request -r --with bootstrap ffmpeg.spec
#	2  bump release of opencv.spec and chromaprint.spec
#	3. make-request -r opencv.spec chromaprint.spec
#	4. bump release of ffmpeg.spec
#	5. make-request -r ffmpeg.spec
#
# Conditional build:
%bcond_with	bootstrap	# disable features to able to build without installed ffmpeg
%bcond_with	nonfree		# unblock non free options of package (currently: cuda_sdk, decklib, fdk_aac, libndi_newtek, npp, openssl)
%bcond_without	bs2b		# BS2B audio filter support
%bcond_without	caca		# textual display using libcaca
%bcond_without	chromaprint	# audio fingerprinting with chromaprint
%bcond_without	cuda		# NVIDIA CUDA code
%bcond_with	cudasdk		# NVIDIA CUDA code using SDK [BR: cuda.h, non-free]
%bcond_with	cuvid		# NVIDIA CUVID support
%bcond_with	decklink	# Blackmagic DeskLink output support (requires nonfree)
%bcond_with	fdk_aac		# AAC de/encoding via libfdk_aac (requires nonfree)
%bcond_without	flite		# flite voice synthesis support
%bcond_without	frei0r		# frei0r video filtering
%bcond_without	fribidi		# fribidi support
%bcond_without	gme		# Game Music Emu support
%bcond_without	ilbc		# iLBC de/encoding via WebRTC libilbc
%bcond_without	kvazaar		# Kvazaar HEVC encoder support
%bcond_without	ladspa		# LADSPA audio filtering
%bcond_with	libdrm		# Linux Direct Rendering Manager code
%bcond_with	librsvg		# SVG rasterization via librsvg
%bcond_with	libxml2		# XML parsing using libxml2
%bcond_with	mfx		# MFX hardware acceleration support
%bcond_with	npp		# NVIDIA Performance Primitives-based code (requires nonfree) [BR: libnppc+libnppi, npp.h]
%bcond_with	nvenc		# NVIDIA NVENC support
%bcond_without	omx		# OpenMAX IL support
%bcond_without	openal		# OpenAL 1.1 capture support
%bcond_without	opencl		# OpenCL 1.2 code
%bcond_without	opencv		# OpenCV video filtering
%bcond_without	opengl		# OpenGL rendering support
%bcond_with	openh264	# OpenH264 H.264 encoder
%bcond_without	openmpt		# OpenMPT module decoder
%bcond_without	pulseaudio	# PulseAudio input support
%bcond_without	rubberband	# rubberband filter
%bcond_without	shine		# shine fixed-point MP3 encoder
%bcond_without	snappy		# Snappy compression support (needed for hap encoding)
%bcond_without	ssh		# SFTP protocol support via libssh
%bcond_with	smb		# SMB support via libsmbclient
%bcond_without	soxr		# SoX Resampler support
%bcond_with	tesseract	# OCR filter based on Tesseract
%bcond_without	x264		# H.264 x264 encoder
%bcond_without	x265		# H.265/HEVC x265 encoder
%bcond_without	va		# VAAPI (Video Acceleration API)
%bcond_without	vidstab		# vid.stab video stabilization support
%bcond_without	vpx		# VP8, a high-quality video codec
%bcond_without	wavpack		# wavpack encoding support
%bcond_without	webp		# WebP encoding support
%bcond_without	zimg		# zscale filter based on z.lib
%bcond_without	zmq		# 0MQ message passing
%bcond_without	zvbi		# teletext via libzvbi
%bcond_without	doc		# don't build docs
%bcond_with	tests		# "make check" (some tests fail as of 2.5)

%if %{with bootstrap}
%undefine	with_opencv
%undefine	with_chromaprint
%endif

%ifnarch %{ix86} %{x8664} %{arm}
%undefine	with_x265
%endif
%ifarch i386 i486
%undefine	with_x265
%endif
Summary:	FFmpeg - a very fast video and audio converter
Summary(pl.UTF-8):	FFmpeg - szybki konwerter audio/wideo
Name:		ffmpeg
Version:	4.0
Release:	2
# LGPL or GPL, chosen at configure time (GPL version is more featured)
# (postprocessing, some filters, x264, x265, xavs, xvid, xcbgrab)
# using v3 allows Apache-licensed libs (opencore-amr, libvo-*enc)
License:	GPL v3+ with LGPL v3+ parts
Group:		Applications/Multimedia
Source0:	http://ffmpeg.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	1cc9e8cb027b9fd4c54f598f51002c19
Patch0:		%{name}-omx-libnames.patch
URL:		http://www.ffmpeg.org/
%{?with_decklink:BuildRequires:	Blackmagic_DeckLink_SDK >= 10.6.1}
%{?with_openal:BuildRequires:	OpenAL-devel >= 1.1}
%{?with_opencl:BuildRequires:	OpenCL-devel >= 1.2}
%{?with_opengl:BuildRequires:	OpenGL-GLX-devel}
# libomxil-bellagio-devel or limoi-core-devel (just headers, library is dlopened at runtime)
%{?with_omx:BuildRequires:	OpenMAX-IL-devel}
BuildRequires:	SDL2-devel >= 2.0.1
BuildRequires:	SDL2-devel < 2.1.0
BuildRequires:	alsa-lib-devel
BuildRequires:	bzip2-devel
BuildRequires:	celt-devel >= 0.11.0
%{?with_fdk_aac:BuildRequires:	fdk-aac-devel}
%{?with_flite:BuildRequires:	flite-devel >= 1.4}
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
%{?with_frei0r:BuildRequires:	frei0r-devel}
%{?with_fribidi:BuildRequires:	fribidi-devel}
%{?with_gme:BuildRequires:	game-music-emu-devel}
%ifarch ppc
# require version with altivec support fixed
BuildRequires:	gcc >= 5:3.3.2-3
%endif
BuildRequires:	gmp-devel
BuildRequires:	gnutls-devel
BuildRequires:	jack-audio-connection-kit-devel
%{?with_kvazaar:BuildRequires:	kvazaar-devel >= 0.8.1}
%{?with_ladspa:BuildRequires:	ladspa-devel}
BuildRequires:	lame-libs-devel >= 3.98.3
BuildRequires:	libass-devel
BuildRequires:	libavc1394-devel
%{?with_bs2b:BuildRequires:	libbs2b-devel}
BuildRequires:	libbluray-devel
%{?with_caca:BuildRequires:	libcaca-devel}
BuildRequires:	libcdio-paranoia-devel >= 0.90-2
%{?with_chromaprint:BuildRequires:	libchromaprint-devel}
BuildRequires:	libdc1394-devel >= 2
%{?with_libdrm:BuildRequires:	libdrm-devel}
BuildRequires:	libgsm-devel
BuildRequires:	libiec61883-devel
BuildRequires:	libmodplug-devel
%{?with_openmpt:BuildRequires: libopenmpt-devel >= 0.2.6557}
BuildRequires:	libraw1394-devel >= 2
%{?with_librsvg:BuildRequires:	librsvg-devel >= 2}
BuildRequires:	librtmp-devel
%{?with_ssh:BuildRequires:	libssh-devel}
%{?with_smb:BuildRequires:	libsmbclient-devel}
BuildRequires:	libtheora-devel >= 1.0-0.beta3
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	libv4l-devel
%if %{with va}
BuildRequires:	libva-devel >= 1.0.3
BuildRequires:	libva-drm-devel >= 1.0.3
BuildRequires:	libva-x11-devel >= 1.0.3
%endif
BuildRequires:	libvdpau-devel >= 0.2
BuildRequires:	libvorbis-devel
%{?with_vpx:BuildRequires:	libvpx-devel >= 1.3.0}
%{?with_webp:BuildRequires:	libwebp-devel >= 0.4.0}
# X264_BUILD >= 118
%{?with_x264:BuildRequires:	libx264-devel >= 0.1.3-1.20111212_2245}
# X265_BUILD >= 68
%{?with_x265:BuildRequires:	libx265-devel >= 1.8}
# libxcb xcb-shm xcb-xfixes xcb-shape
BuildRequires:	libxcb-devel >= 1.4
%{?with_libxml2:BuildRequires:	libxml2-devel >= 2}
%{?with_mfx:BuildRequires:	mfx_dispatch-devel}
%ifarch %{ix86}
%ifnarch i386 i486
BuildRequires:	nasm
%endif
%endif
# which package?
#%{?with_nvenc:BuildRequires:	NVIDIA-NVENC-API} compat/nvenc/nvEncodeAPI.h
BuildRequires:	opencore-amr-devel
%{?with_opencv:BuildRequires:	opencv-devel}
%{?with_openh264:BuildRequires:	openh264-devel >= 1.3}
BuildRequires:	openjpeg2-devel >= 2.1
BuildRequires:	opus-devel
BuildRequires:	perl-Encode
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel}
BuildRequires:	rpmbuild(macros) >= 1.470
%{?with_rubberband:BuildRequires:	rubberband-devel >= 1.8.1}
%{?with_shine:BuildRequires:	shine-devel >= 3.0.0}
%{?with_snappy:BuildRequires:	snappy-devel}
%{?with_soxr:BuildRequires:	soxr-devel}
BuildRequires:	speex-devel >= 1:1.2-rc1
%{?with_tesseract:BuildRequires:	tesseract-devel}
%{?with_doc:BuildRequires:	tetex}
%{?with_doc:BuildRequires:	texi2html}
%{?with_doc:BuildRequires:	texinfo}
BuildRequires:	twolame-devel
%{?with_vidstab:BuildRequires:	vid.stab-devel >= 0.98}
BuildRequires:	vo-amrwbenc-devel
%{?with_wavpack:BuildRequires:	wavpack-devel}
%{?with_ilbc:BuildRequires:	webrtc-libilbc-devel}
BuildRequires:	xavs-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xvid-devel >= 1:1.1.0
BuildRequires:	xz-devel
BuildRequires:	yasm
%{?with_zmq:BuildRequires:	zeromq-devel}
%{?with_zimg:BuildRequires:	zimg-devel >= 2.7.0}
BuildRequires:	zlib-devel
%{?with_zvbi:BuildRequires:	zvbi-devel}
%{?with_autoreqdep:BuildConflicts:	libpostproc}
# overflows maximum hash table size
BuildConflicts:	pdksh < 5.2.14-57
Requires:	%{name}-libs = %{version}-%{release}
%{?with_ilbc:Requires:	webrtc-libilbc}
Requires:	xvid >= 1:1.1.0
Obsoletes:	libpostproc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	SDL2 >= 2.0.1
%if "%(rpm -q --qf '%{V}' gnutls-devel)" >= "3.0.20"
# uses gnutls_certificate_set_x509_system_trust if >= 3.0.20
Requires:	gnutls-libs >= 3.0.20
%endif
%{?with_openmpt:Requires: libopenmpt >= 0.2.6557}
%{?with_vpx:Requires:	libvpx >= 1.3.0}
%{?with_rubberband:Requires:	rubberband-libs >= 1.8.1}
%{?with_zimg:Requires:	zimg >= 2.7.0}

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
%{?with_opencl:Requires:	OpenCL-devel >= 1.2}
%{?with_opengl:Requires:	OpenGL-devel}
Requires:	SDL2-devel >= 2.0.1
Requires:	alsa-lib-devel
Requires:	bzip2-devel
Requires:	celt-devel >= 0.11.0
%{?with_fdk_aac:Requires:	fdk-aac-devel}
%{?with_flite:Requires:	flite-devel >= 1.4}
Requires:	fontconfig-devel
Requires:	freetype-devel
%{?with_fribidi:Requires:	fribidi-devel}
%{?with_gme:Requires:	game-music-emu-devel}
Requires:	jack-audio-connection-kit-devel
%{?with_kvazaar:Requires:	kvazaar-devel >= 0.8.1}
Requires:	lame-libs-devel >= 3.98.3
Requires:	libass-devel
Requires:	libavc1394-devel
Requires:	libbluray-devel
%{?with_bs2b:Requires:	libbs2b-devel}
%{?with_caca:Requires:	libcaca-devel}
Requires:	libcdio-paranoia-devel >= 0.90-2
%{?with_chromaprint:Requires:	libchromaprint-devel}
Requires:	libdc1394-devel >= 2
%{?with_libdrm:Requires:	libdrm-devel}
Requires:	libgsm-devel
Requires:	libiec61883-devel
Requires:	libmodplug-devel
%{?with_openmpt:Requires: libopenmpt-devel >= 0.2.6557}
Requires:	libraw1394-devel >= 2
%{?with_librsvg:Requires:	librsvg-devel >= 2}
Requires:	librtmp-devel
%{?with_smb:Requires:	libsmbclient-devel}
Requires:	libtheora-devel >= 1.0-0.beta3
%{?with_va:Requires:	libva-devel >= 1.0.3}
Requires:	libvorbis-devel
%{?with_vpx:Requires:	libvpx-devel >= 1.3.0}
%{?with_webp:Requires:	libwebp-devel >= 0.4.0}
%{?with_x264:Requires:	libx264-devel >= 0.1.3-1.20110625_2245}
%{?with_x265:Requires:	libx265-devel >= 1.8}
%{?with_libxml2:Requires:	libxml2-devel >= 2}
%{?with_mfx:Requires:	mfx_dispatch-devel}
Requires:	opencore-amr-devel
%{?with_opencv:Requires:	opencv-devel}
%{?with_openh264:Requires:	openh264-devel >= 1.3}
Requires:	openjpeg2-devel >= 2.1
%{?with_rubberband:Requires:	rubberband-devel >= 1.8.1}
%{?with_shine:Requires:	shine-devel >= 3.0.0}
%{?with_snappy:Requires:	snappy-devel}
%{?with_soxr:Requires:	soxr-devel}
Requires:	speex-devel >= 1:1.2-rc1
%{?with_tesseract:Requires:	tesseract-devel}
Requires:	twolame-devel
%{?with_vidstab:Requires:	vid.stab-devel >= 0.98}
Requires:	vo-amrwbenc-devel
%{?with_wavpack:Requires:	wavpack-devel}
%{?with_ilbc:Requires:	webrtc-libilbc-devel}
Requires:	xavs-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xvid-devel >= 1:1.1.0
%{?with_zmq:Requires:	zeromq-devel}
%{?with_zimg:Requires:	zimg-devel >= 2.3.0}
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

%package doc
Summary:	FFmpeg documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja pakietu FFmpeg w formacie HTML
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
FFmpeg documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja pakietu FFmpeg w formacie HTML.

%prep
%setup -q
%patch0 -p1

# package the grep result for mplayer, the result formatted as ./mplayer/configure
cat <<EOF > ffmpeg-avconfig
#! /bin/sh
libavdecoders_all="$(sed -n 's/^[^#]*DEC.*(.*, *\(.*\)).*/\1_decoder/p' libavcodec/allcodecs.c | tr '[a-z]' '[A-Z]')"
libavencoders_all="$(sed -n 's/^[^#]*ENC.*(.*, *\(.*\)).*/\1_encoder/p' libavcodec/allcodecs.c | tr '[a-z]' '[A-Z]')"
libavparsers_all="$(sed -n 's/^[^#]*PARSER.*(.*, *\(.*\)).*/\1_parser/p' libavcodec/allcodecs.c | tr '[a-z]' '[A-Z]')"
libavbsfs_all="$(sed -n 's/^[^#]*BSF.*(.*, *\(.*\)).*/\1_bsf/p' libavcodec/allcodecs.c | tr '[a-z]' '[A-Z]')"
libavdemuxers_all="$(sed -n 's/^[^#]*DEMUX.*(.*, *\(.*\)).*/\1_demuxer/p' libavformat/allformats.c | tr '[a-z]' '[A-Z]')"
libavmuxers_all="$(sed -n 's/^[^#]*_MUX.*(.*, *\(.*\)).*/\1_muxer/p' libavformat/allformats.c | tr '[a-z]' '[A-Z]')"
libavprotocols_all="$(sed -n 's/^[^#]*PROTOCOL.*(.*, *\(.*\)).*/\1_protocol/p' libavformat/allformats.c | tr '[a-z]' '[A-Z]')"
libavhwaccels_all="$(sed -n 's/^[^#]*HWACCEL.*(.*, *\(.*\)).*/\1_hwaccel/p' libavcodec/allcodecs.c | tr '[a-z]' '[A-Z]')"
libavfilters_all="$(sed -n 's/^[^#]*FILTER.*(.*, *\(.*\),.*).*/\1_filter/p' libavfilter/allfilters.c | tr '[a-z]' '[A-Z]')"
EOF
cat <<'EOF' >> ffmpeg-avconfig

case "$1" in
--decoders)
	echo $libavdecoders_all
	;;
--encoders)
	echo $libavencoders_all
	;;
--parsers)
	echo $libavparsers_all
	;;
--bsfs)
	echo $libavbsfs_all
	;;
--demuxers)
	echo $libavdemuxers_all
	;;
--muxers)
	echo $libavmuxers_all
	;;
--protocols)
	echo $libavprotocols_all
	;;
--hwaccels)
	echo $libavhwaccels_all
	;;
--filters)
	echo $libavfilters_all
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
  --hwaccels
  --filters
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
	--extra-cflags="-D_GNU_SOURCE=1 %{rpmcppflags} %{rpmcflags}%{?with_decklink: -I/usr/include/decklink}" \
	--extra-ldflags="%{rpmcflags} %{rpmldflags}" \
	--cc="%{__cc}" \
	--disable-debug \
	--disable-optimizations \
	--disable-stripping \
	%{!?with_doc:--disable-doc} \
	--enable-avfilter \
	--enable-avresample \
	%{?with_chromaprint:--enable-chromaprint} \
	%{!?with_cuda:--disable-cuda} \
	%{?with_cudasdk:--enable-cuda-sdk} \
	%{!?with_cuvid:--disable-cuvid} \
	%{?with_decklink:--enable-decklink} \
	--enable-gnutls \
	--enable-gpl \
	--enable-version3 \
	%{?with_frei0r:--enable-frei0r} \
	%{?with_ladspa:--enable-ladspa} \
	--enable-libass \
	--enable-libbluray \
	%{?with_bs2b:--enable-libbs2b} \
	%{?with_caca:--enable-libcaca} \
	--enable-libcelt \
	--enable-libcdio \
	--enable-libdc1394 \
	%{?with_libdrm:--enable-libdrm} \
	%{?with_flite:--enable-libflite} \
	--enable-libfontconfig \
	--enable-libfreetype \
	%{?with_fribidi:--enable-libfribidi} \
	%{?with_gme:--enable-libgme} \
	--enable-libgsm \
	--enable-libiec61883 \
	%{?with_ilbc:--enable-libilbc} \
	%{?with_kvazaar:--enable-libkvazaar} \
	%{?with_mfx:--enable-libmfx} \
	--enable-libmodplug \
	--enable-libmp3lame \
	--enable-libopencore-amrnb \
	--enable-libopencore-amrwb \
	%{?with_opencv:--enable-libopencv} \
	%{?with_openh264:--enable-libopenh264} \
	--enable-libopenjpeg \
	%{?with_openmpt:--enable-libopenmpt} \
	--enable-libopus \
	%{?with_pulseaudio:--enable-libpulse} \
	%{?with_librsvg:--enable-librsvg} \
	--enable-librtmp \
	%{?with_libxml2:--enable-libxml2} \
	%{?with_rubberband:--enable-librubberband} \
	%{?with_shine:--enable-libshine} \
	%{?with_smb:--enable-libsmbclient} \
	%{?with_snappy:--enable-libsnappy} \
	%{?with_soxr:--enable-libsoxr} \
	--enable-libspeex \
	%{?with_ssh:--enable-libssh} \
	%{?with_tesseract:--enable-libtesseract} \
	--enable-libtheora \
	--enable-libtwolame \
	--enable-libv4l2 \
	%{?with_vidstab:--enable-libvidstab} \
	--enable-libvo-amrwbenc \
	--enable-libvorbis \
	%{?with_vpx:--enable-libvpx} \
	%{?with_wavpack:--enable-libwavpack} \
	%{?with_webp:--enable-libwebp} \
	%{?with_x264:--enable-libx264} \
	%{?with_x265:--enable-libx265} \
	--enable-libxavs \
	--enable-libxcb \
	--enable-libxvid \
	%{?with_zimg:--enable-libzimg} \
	%{?with_zmq:--enable-libzmq} \
	%{?with_zvbi:--enable-libzvbi} \
	%{!?with_nvenc:--disable-nvenc} \
	%{?with_omx:--enable-omx} \
	%{?with_openal:--enable-openal} \
	%{?with_opencl:--enable-opencl} \
	%{?with_opengl:--enable-opengl} \
	--enable-postproc \
	--enable-pthreads \
	--enable-shared \
	--enable-swscale \
	%{!?with_va:--disable-vaapi} \
%ifnarch %{ix86} %{x8664}
	--disable-mmx \
%endif
%ifarch i386 i486
	--disable-mmx \
%endif
%ifarch x32
	--disable-asm \
%endif
%if %{with nonfree}
	--enable-nonfree \
	%{?with_fdk_aac:--enable-libfdk-aac} \
	%{?with_npp:--enable-libnpp} \
%endif
	--enable-runtime-cpudetect

%{__make} \
	V=1

# CC_O to add -c to commandline. makefile should be patched
%{__make} tools/qt-faststart V=1 CC_O='-c -o $@'

%{?with_tests:%{__make} check V=1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},/etc/{sysconfig,rc.d/init.d}} \
	$RPM_BUILD_ROOT%{_includedir}/ffmpeg

%{__make} install install-headers \
	DESTDIR=$RPM_BUILD_ROOT \
	V=1

# install nonstandard, non-public headers manually
cp -a config.h $RPM_BUILD_ROOT%{_includedir}/ffmpeg
for a in libavutil/*/{asm,bswap}.h; do
	install -Dp $a $RPM_BUILD_ROOT%{_includedir}/$a
done
cp -a libavformat/riff.h $RPM_BUILD_ROOT%{_includedir}/libavformat

install -p tools/qt-faststart $RPM_BUILD_ROOT%{_bindir}

# install as ffmpeg-avconfig to avoid with possible programs looking for
# ffmpeg-config and expecting --libs output from it which is not implemented
# simple to do (by querying pkgconfig), but why?
install -p ffmpeg-avconfig $RPM_BUILD_ROOT%{_bindir}/ffmpeg-avconfig

# packaged as %doc in -doc
%if %{with doc}
%{__rm} $RPM_BUILD_ROOT%{_docdir}/ffmpeg/*.html
%endif

install -d $RPM_BUILD_ROOT%{_examplesdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/ffmpeg/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS LICENSE.md MAINTAINERS README.md RELEASE_NOTES doc/APIchanges
%attr(755,root,root) %{_bindir}/ffmpeg
%attr(755,root,root) %{_bindir}/ffprobe
%attr(755,root,root) %{_bindir}/qt-faststart
%dir %{_datadir}/ffmpeg
%{_datadir}/ffmpeg/*.ffpreset
%{_datadir}/ffmpeg/ffprobe.xsd
%if %{with doc}
%{_mandir}/man1/ffmpeg.1*
%{_mandir}/man1/ffmpeg-all.1*
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
%{_mandir}/man1/ffprobe-all.1*
%endif

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavcodec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavcodec.so.58
%attr(755,root,root) %{_libdir}/libavdevice.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavdevice.so.58
%attr(755,root,root) %{_libdir}/libavfilter.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavfilter.so.7
%attr(755,root,root) %{_libdir}/libavformat.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavformat.so.58
%attr(755,root,root) %{_libdir}/libavresample.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavresample.so.4
%attr(755,root,root) %{_libdir}/libavutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavutil.so.56
%attr(755,root,root) %{_libdir}/libpostproc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpostproc.so.55
%attr(755,root,root) %{_libdir}/libswresample.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libswresample.so.3
%attr(755,root,root) %{_libdir}/libswscale.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libswscale.so.5

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
%{_examplesdir}/%{name}-%{version}

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
%if %{with doc}
%{_mandir}/man1/ffplay.1*
%{_mandir}/man1/ffplay-all.1*
%endif

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc doc/*.html
%endif
