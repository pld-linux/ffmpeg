# TODO:
# - libopenvino
# - libtensorflow [-ltensorflow tensorflow/c/c_api.h]
# - AMF >= 1.4.29.0 (available at https://github.com/GPUOpen-LibrariesAndSDKs/AMF, where is original source?)
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
%bcond_with	nonfree		# unblock non free options of package (currently: cuda_nvcc, decklib, fdk_aac, npp, openssl, libressl/libtls)
%bcond_without	amr		# AMR-NB/WB de/encoding via libopencore-amrnb/wb
%bcond_without	aom		# AV1 viden de/encoding via libaom
%bcond_without	aribb24		# ARIB text and caption decoding via libaribb24
%bcond_without	avisynth	# AviSynth scripts support
%bcond_without	avs		# AVS encoding via xavs
%bcond_without	avs2		# AVS2 de/encoding via libdavs2/libxavs2
%bcond_without	bs2b		# BS2B audio filter support
%bcond_without	caca		# textual display using libcaca
%bcond_without	codec2		# codec2 support using libcodec2
%bcond_without	chromaprint	# audio fingerprinting with chromaprint
%bcond_with	cudasdk		# NVIDIA CUDA code using nvcc from CUDA SDK [BR: cuda.h, non-free]
%bcond_with	dav1d		# AV1 decoding via libdav1d
%bcond_without	dc1394		# IIDC-1394 grabbing using libdc1394
%bcond_with	decklink	# Blackmagic DeckLink I/O support (requires nonfree)
%bcond_with	fdk_aac		# AAC de/encoding via libfdk_aac (requires nonfree)
%bcond_without	ffnvcodec	# NVIDIA codecs support using ffnvcodec headers (covered: cuda cuvid nvdec nvenc)
%bcond_without	flite		# flite voice synthesis support
%bcond_without	frei0r		# frei0r video filtering
%bcond_without	fribidi		# fribidi support in drawtext filter
%bcond_with	glslang		# GLSL->SPIRV compilation via libglslang
%bcond_without	gme		# Game Music Emu support
%bcond_without	gsm		# GSM de/encoding via libgsm
%bcond_without	iec61883	# ec61883 via libiec61883
%bcond_without	ilbc		# iLBC de/encoding via WebRTC libilbc
%bcond_without	kvazaar		# Kvazaar HEVC encoder support
%bcond_without	ladspa		# LADSPA audio filtering
%bcond_without	lcms		# ICC profile support via lcms2
%bcond_with	lensfun		# lensfun lens correction
%bcond_with	libaribcaption	# ARIB text and caption decoding via libaribcaption
%bcond_with	libdrm		# Linux Direct Rendering Manager code
%bcond_without	libjxl		# JPEG XL de/encoding via libjxl
%bcond_with	libklvanc	# Kernel Labs VANC processing (in decklink driver)
%bcond_without	libmysofa	# sofalizer filter
%bcond_with	libplacebo	# libplacebo filters
%bcond_without	librist		# RIST support via librist
%bcond_with	librsvg		# SVG rasterization via librsvg
%bcond_with	libxml2		# XML parsing using libxml2
%bcond_without	lv2		# LV2 audio filtering
%bcond_with	mfx		# MFX hardware acceleration support
%bcond_without	modplug		# ModPlug via libmodplug
%bcond_with	npp		# NVIDIA Performance Primitives-based code (requires nonfree) [BR: libnppc+libnppi, npp.h]
%bcond_without	omx		# OpenMAX IL support
%bcond_without	openal		# OpenAL 1.1 capture support
%bcond_without	opencl		# OpenCL 1.2 code
%bcond_with	opencv		# OpenCV video filtering
%bcond_without	opengl		# OpenGL rendering support
%bcond_with	openh264	# OpenH264 H.264 encoder
%bcond_without	openmpt		# OpenMPT module decoder
%bcond_with	pocketsphinx	# asr filter using PocketSphinx
%bcond_without	pulseaudio	# PulseAudio input support
%bcond_without	rabbitmq	# RabbitMQ support
%bcond_with	rav1e		# AV1 encoding using rav1e
%bcond_with	rkmpp		# Rockchip Media Process Platform code [implies libdrm]
%bcond_without	rubberband	# rubberband filter
%bcond_without	shaderc		# GLSL->SPIRV compilation via libshaderc
%bcond_without	shine		# shine fixed-point MP3 encoder
%bcond_with	smb		# SMB support via libsmbclient
%bcond_without	snappy		# Snappy compression support (needed for hap encoding)
%bcond_without	soxr		# SoX Resampler support
%bcond_without	srt		# Haivision SRT protocol support
%bcond_without	ssh		# SFTP protocol support via libssh
%bcond_with	svtav1		# AV1 encoding via SVT-AV1
%bcond_with	tesseract	# OCR filter based on Tesseract
%bcond_without	theora		# Theora encoding via libtheora
%bcond_with	uavs3d		# AVS3 decoding via libuavs3d (TODO: enable when 1.1.41 released)
%bcond_with	v4l2_request	# V4L2 request API for stateless hw decoding
%bcond_without	va		# VAAPI (Video Acceleration API)
%bcond_without	vapoursynth	# VapourSynth demuxer
%bcond_without	vidstab		# vid.stab video stabilization support
%bcond_without	vmaf		# VMAF filter support
%bcond_without	voamrwbenc	# MR-WB encoding via libvo-amrwbenc
%bcond_with	vpl		# libvpl instead of MFX
%bcond_without	vpx		# VP8, a high-quality video codec
%bcond_without	vulkan		# Vulkan code
%bcond_without	webp		# WebP encoding support
%bcond_without	x264		# H.264 x264 encoder
%bcond_without	x265		# H.265/HEVC x265 encoder
%bcond_without	xvid		# vid encoding via xvidcore
%bcond_without	zimg		# zscale filter based on z.lib
%bcond_without	zmq		# 0MQ message passing
%bcond_without	zvbi		# teletext via libzvbi
%bcond_without	doc		# HTML documentation
%bcond_without	static_libs	# static libraries
%bcond_with	tests		# "make check" (some tests fail as of 2.5)

%if %{with bootstrap}
%undefine	with_opencv
%undefine	with_chromaprint
%endif
%if %{with rkmpp} || %{with v4l2_request}
%define		with_libdrm	1
%endif
%if %{with glslang}
%undefine	with_shaderc
%endif
%if %{with vpl}
%undefine	with_mfx
%endif

%ifnarch %{ix86} %{x8664}
%undefine	with_ffnvcodec
%endif
%ifnarch %{ix86} %{x8664} aarch64
%undefine	with_rav1e
%endif
%ifnarch %{ix86} %{x8664} x32 %{arm} aarch64
%undefine	with_x265
%endif
%ifarch i386 i486
%undefine	with_x265
%endif
%ifarch i686 pentium4 athlon %{x8664} x32
%define		with_crystalhd	1
%endif
Summary:	FFmpeg - a very fast video and audio converter
Summary(pl.UTF-8):	FFmpeg - szybki konwerter audio/wideo
Name:		ffmpeg
# NOTE: 7.x prepared on DEVEL-7.1 branch, but other software is not ready (e.g. xine-lib 1.2.13, gstreamer-libav 1.24.2)
Version:	6.1.3
Release:	2
# LGPL or GPL, chosen at configure time (GPL version is more featured)
# GPL: frei0r libcdio libdavs2 rubberband vidstab x264 x265 xavs xavs2 xvid
# v3 (allows *GPLv3 or Apache-licensed libs): gmp lensfun opencore-amr vmaf vo-*enc rkmpp
# GPLv3: smbclient
License:	GPL v3+ with LGPL v3+ parts
Group:		Applications/Multimedia
Source0:	https://ffmpeg.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	f1fa311d96f576f700bc830d1ed86e0c
Patch0:		%{name}-omx-libnames.patch
Patch1:		%{name}-atadenoise.patch
Patch2:		opencv4.patch
Patch3:		v4l2-request-hwdec.patch
Patch4:		ffmpeg-vulkan1.3.280.patch
Patch5:		gcc14.patch
Patch6:		texinfo-7.2.patch
Patch7:		libv4l2-1.30.patch
URL:		https://ffmpeg.org/
%{?with_avisynth:BuildRequires:	AviSynthPlus-devel >= 3.7.3}
%{?with_decklink:BuildRequires:	Blackmagic_DeckLink_SDK >= 10.11}
%{?with_openal:BuildRequires:	OpenAL-devel >= 1.1}
%{?with_opencl:BuildRequires:	OpenCL-devel >= 1.2}
%{?with_opengl:BuildRequires:	OpenGL-GLX-devel}
# libomxil-bellagio-devel or limoi-core-devel (just headers, library is dlopened at runtime)
%{?with_omx:BuildRequires:	OpenMAX-IL-devel}
BuildRequires:	SDL2-devel >= 2.0.1
BuildRequires:	SDL2-devel < 3.0.0
%{?with_vulkan:BuildRequires:	Vulkan-Loader-devel >= 1.3.277}
BuildRequires:	alsa-lib-devel
%{?with_aom:BuildRequires:	aom-devel >= 1.0.0}
%{?with_aribb24:BuildRequires:	aribb24-devel}
BuildRequires:	bzip2-devel
BuildRequires:	celt-devel >= 0.11.0
%{?with_codec2:BuildRequires:	codec2-devel}
%{?with_dav1d:BuildRequires:	dav1d-devel >= 0.5.0}
%{?with_avs2:BuildRequires:	davs2-devel >= 1.6}
%{?with_fdk_aac:BuildRequires:	fdk-aac-devel}
%{?with_flite:BuildRequires:	flite-devel >= 1.4}
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
%{?with_frei0r:BuildRequires:	frei0r-devel}
%{?with_fribidi:BuildRequires:	fribidi-devel}
%{?with_gme:BuildRequires:	game-music-emu-devel}
BuildRequires:	harfbuzz-devel
%ifarch ppc
# require version with altivec support fixed
BuildRequires:	gcc >= 5:3.3.2-3
%endif
%{?with_glslang:BuildRequires:	glslang-devel >= 11}
BuildRequires:	gmp-devel
BuildRequires:	gnutls-devel
BuildRequires:	jack-audio-connection-kit-devel
%{?with_kvazaar:BuildRequires:	kvazaar-devel >= 2.0.0}
%{?with_ladspa:BuildRequires:	ladspa-devel}
BuildRequires:	lame-libs-devel >= 3.98.3
%{?with_lcms:BuildRequires:	lcms2-devel >= 2.13}
%{?with_lensfun:BuildRequires:	lensfun-devel >= 0.3.95}
%{?with_aribcaption:BuildRequires:	libaribcaption-devel}
BuildRequires:	libass-devel >= 0.11.0
%ifnarch %arch_with_atomics64
BuildRequires:	libatomic-devel
%endif
%{?with_iec61883:BuildRequires:	libavc1394-devel}
%{?with_bs2b:BuildRequires:	libbs2b-devel}
BuildRequires:	libbluray-devel
%{?with_caca:BuildRequires:	libcaca-devel}
BuildRequires:	libcdio-paranoia-devel >= 0.90-2
%{?with_chromaprint:BuildRequires:	libchromaprint-devel}
%{?with_crystalhd:BuildRequires:	libcrystalhd-devel}
%{?with_dc1394:BuildRequires:	libdc1394-devel >= 2}
%{?with_libdrm:BuildRequires:	libdrm-devel}
%{?with_gsm:BuildRequires:	libgsm-devel}
%{?with_iec61883:BuildRequires:	libiec61883-devel}
%{?with_libjxl:BuildRequires:	libjxl-devel >= 0.7.0}
%{?with_libklvanc:BuildRequires:	libklvanc-devel}
%{?with_modplug:BuildRequires:	libmodplug-devel}
%{?with_libmysofa:BuildRequires:	libmysofa-devel >= 0.7}
%{?with_openmpt:BuildRequires: libopenmpt-devel >= 0.4.5}
%{?with_libplacebo:BuildRequires:	libplacebo-devel >= 4.192.0}
%if %{with dc1394} || %{with iec61883}
BuildRequires:	libraw1394-devel >= 2
%endif
%{?with_librist:BuildRequires:	librist-devel >= 0.2.7}
%{?with_librsvg:BuildRequires:	librsvg-devel >= 2}
BuildRequires:	librtmp-devel
%{?with_ssh:BuildRequires:	libssh-devel >= 0.6.0}
%{?with_smb:BuildRequires:	libsmbclient-devel}
%{?with_theora:BuildRequires:	libtheora-devel >= 1.0-0.beta3}
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	libv4l-devel
%if %{with va}
BuildRequires:	libva-devel >= 1.0.3
BuildRequires:	libva-drm-devel >= 1.0.3
BuildRequires:	libva-x11-devel >= 1.0.3
%endif
BuildRequires:	libvdpau-devel >= 1.3
BuildRequires:	libvorbis-devel
%{?with_vpl:BuildRequires:	libvpl-devel >= 2.6}
%{?with_vpx:BuildRequires:	libvpx-devel >= 1.4.0}
%{?with_webp:BuildRequires:	libwebp-devel >= 0.4.0}
# X264_BUILD >= 122
%{?with_x264:BuildRequires:	libx264-devel >= 0.1.3-1.20130827_2245}
# X265_BUILD >= 89
%{?with_x265:BuildRequires:	libx265-devel >= 2.0}
# libxcb xcb-shm xcb-xfixes xcb-shape
BuildRequires:	libxcb-devel >= 1.4
%{?with_libxml2:BuildRequires:	libxml2-devel >= 2}
%{?with_lv2:BuildRequires:	lilv-devel}
%{?with_v4l2_request:BuildRequires:	linux-libc-headers >= 7:5.11.0}
%{?with_lv2:BuildRequires:	lv2-devel}
%{?with_mfx:BuildRequires:	mfx_dispatch-devel >= 1.28}
%ifarch %{ix86}
%ifnarch i386 i486
BuildRequires:	nasm
%endif
%endif
%{?with_ffnvcodec:BuildRequires:	nv-codec-headers >= 12.1.14.0}
# amrnb,amrwb
%{?with_amr:BuildRequires:	opencore-amr-devel}
%{?with_opencv:BuildRequires:	opencv-devel >= 2}
%{?with_openh264:BuildRequires:	openh264-devel >= 1.3}
BuildRequires:	openjpeg2-devel >= 2.1
BuildRequires:	opus-devel
BuildRequires:	perl-Encode
BuildRequires:	perl-tools-pod
%{?with_pocketsphinx:BuildRequires:	pocketsphinx-devel > 0.8}
BuildRequires:	pkgconfig
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel}
%{?with_rabbitmq:BuildRequires:	rabbitmq-c-devel >= 0.7.1}
%{?with_rav1e:BuildRequires:	rav1e-devel >= 0.5.0}
%{?with_rkmpp:BuildRequires:	rockchip-mpp-devel >= 1.3.7}
BuildRequires:	rpmbuild(macros) >= 2.025
%{?with_rubberband:BuildRequires:	rubberband-devel >= 1.8.1}
%{?with_shaderc:BuildRequires:	shaderc-devel >= 2019.1}
%{?with_shine:BuildRequires:	shine-devel >= 3.0.0}
%{?with_snappy:BuildRequires:	snappy-devel}
%{?with_soxr:BuildRequires:	soxr-devel}
BuildRequires:	speex-devel >= 1:1.2-rc1
%{?with_glslang:BuildRequires:	spirv-tools-devel}
%{?with_srt:BuildRequires:	srt-devel >= 1.3}
%{?with_svtav1:BuildRequires:	svt-av1-devel >= 0.9.0}
BuildRequires:	tar >= 1:1.22
%{?with_tesseract:BuildRequires:	tesseract-devel}
%{?with_doc:BuildRequires:	tetex}
%{?with_doc:BuildRequires:	texi2html}
%{?with_doc:BuildRequires:	texinfo}
BuildRequires:	twolame-devel >= 0.3.10
%{?with_uavs3d:BuildRequires:	uavs3d-devel >= 1.1.41}
%{?with_v4l2_request:BuildRequires:	udev-devel}
%{?with_vapoursynth:BuildRequires:	vapoursynth-devel >= 42}
%{?with_vidstab:BuildRequires:	vid.stab-devel >= 0.98}
%{?with_vmaf:BuildRequires:	vmaf-devel >= 2.0.0}
%{?with_voamrwbenc:BuildRequires:	vo-amrwbenc-devel}
%{?with_ilbc:BuildRequires:	webrtc-libilbc-devel}
%{?with_avs:BuildRequires:	xavs-devel}
%{?with_avs2:BuildRequires:	xavs2-devel >= 1.3}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
%{?with_xvid:BuildRequires:	xvid-devel >= 1:1.1.0}
BuildRequires:	xz
BuildRequires:	xz-devel
%{?with_zmq:BuildRequires:	zeromq-devel >= 4.2.1}
%{?with_zimg:BuildRequires:	zimg-devel >= 2.7.0}
BuildRequires:	zlib-devel
%{?with_zvbi:BuildRequires:	zvbi-devel >= 0.2.28}
# overflows maximum hash table size
BuildConflicts:	pdksh < 5.2.14-57
Requires:	%{name}-libs = %{version}-%{release}
Suggests:	fontconfig
Suggests:	fonts-TTF-Roboto
Obsoletes:	libpostproc < 2:1.0-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing -fPIC

# -fomit-frame-pointer is always needed on x86 due to lack of registers (-fPIC takes one)
%define		specflags_ia32	-fomit-frame-pointer
# -mmmx is needed to enable <mmintrin.h> code.
%define		specflags_i586	-mmmx
%define		specflags_i686	-mmmx

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
%{?with_vulkan:Requires:	Vulkan-Loader >= 1.3.277}
%{?with_aom:Requires:	aom >= 1.0.0}
Requires:	celt >= 0.11.0
%{?with_dav1d:Requires:	dav1d >= 0.5.0}
%{?with_avs2:Requires:	davs2 >= 1.6}
%{?with_flite:Requires:	flite >= 1.4}
%if "%(rpm -q --qf '%{V}' gnutls-devel)" >= "3.0.20"
# uses gnutls_certificate_set_x509_system_trust if >= 3.0.20
Requires:	gnutls-libs >= 3.0.20
%endif
%{?with_kvazaar:Requires:	kvazaar-libs >= 2.0.0}
Requires:	libass >= 0.11.0
%{?with_libjxl:Requires:	libjxl >= 0.7.0}
%{?with_libmysofa:Requires:	libmysofa >= 0.7}
%{?with_openmpt:Requires: libopenmpt >= 0.4.5}
%{?with_libplacebo:Requires:	libplacebo >= 4.192.0}
%{?with_librist:Requires:	librist >= 0.2.7}
%{?with_ssh:Requires:	libssh >= 0.6.0}
%{?with_theora:Requires:	libtheora >= 1.0-0.beta3}
%if %{with va}
Requires:	libva >= 1.0.3
Requires:	libva-drm >= 1.0.3
Requires:	libva-x11 >= 1.0.3
%endif
Requires:	libvdpau >= 1.3
%{?with_vpl:Requires:	libvpl >= 2.6}
%{?with_vpx:Requires:	libvpx >= 1.4.0}
%{?with_webp:Requires:	libwebp >= 0.4.0}
%{?with_x264:Requires:	libx264 >= 0.1.3-1.20130827_2245}
%{?with_x265:Requires:	libx265 >= 2.0}
Requires:	libxcb >= 1.4
Requires:	lame-libs >= 3.98.3
%{?with_lcms:Requires:	lcms2 >= 2.13}
%{?with_mfx:Requires:	mfx_dispatch >= 1.28}
%{?with_openh264:Requires:	openh264 >= 1.3}
Requires:	openjpeg2 >= 2.1
%{?with_rabbitmq:Requires:	rabbitmq-c >= 0.7.1}
%{?with_rav1e:Requires:	rav1e-libs >= 0.5.0}
%{?with_rkmpp:Requires:	rockchip-mpp >= 1.3.7}
%{?with_rubberband:Requires:	rubberband-libs >= 1.8.1}
%{?with_shine:Requires:	shine >= 3.0.0}
Requires:	speex >= 1:1.2-rc1
%{?with_srt:Requires:	srt >= 1.3}
%{?with_svtav1:Requires:	svt-av1 >= 0.9.0}
Requires:	twolame-libs >= 0.3.10
%{?with_uavs3d:Requires:	uavs3d >= 1.1.41}
%{?with_vapoursynth:Requires:	vapoursynth >= 42}
%{?with_vidstab:Requires:	vid.stab >= 0.98}
%{?with_vmaf:Requires:	vmaf-libs >= 2.0.0}
%{?with_avs2:Requires:	xavs2 >= 1.3}
%{?with_xvid:Requires:	xvid >= 1:1.1.0}
%{?with_zmq:Requires:	zeromq >= 4.2.1}
%{?with_zimg:Requires:	zimg >= 2.7.0}
%{?with_zvbi:Requires:	zvbi >= 0.2.28}
# dlopened
%{?with_avisynth:Suggests:	AviSynthPlus >= 3.7.3}

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
# Libs.private from *.pc
%{?with_openal:Requires:	OpenAL-devel >= 1.1}
%{?with_opencl:Requires:	OpenCL-devel >= 1.2}
%{?with_opengl:Requires:	OpenGL-devel}
Requires:	SDL2-devel >= 2.0.1
%{?with_vulkan:Requires:	Vulkan-Loader-devel >= 1.3.277}
Requires:	alsa-lib-devel
%{?with_aom:Requires:	aom-devel >= 1.0.0}
%{?with_aribb24:Requires:	aribb24-devel}
Requires:	bzip2-devel
Requires:	celt-devel >= 0.11.0
%{?with_codec2:Requires:	codec2-devel}
%{?with_dav1d:Requires:	dav1d-devel >= 0.5.0}
%{?with_avs2:Requires:	davs2-devel >= 1.6}
%{?with_fdk_aac:Requires:	fdk-aac-devel}
%{?with_flite:Requires:	flite-devel >= 1.4}
Requires:	fontconfig-devel
Requires:	freetype-devel
%{?with_fribidi:Requires:	fribidi-devel}
%{?with_gme:Requires:	game-music-emu-devel}
%{?with_glslang:Requires:	glslang-devel}
Requires:	gnutls-devel
Requires:	harfbuzz-devel
Requires:	jack-audio-connection-kit-devel
%{?with_kvazaar:Requires:	kvazaar-devel >= 2.0.0}
Requires:	lame-libs-devel >= 3.98.3
%{?with_lcms:Requires:	lcms2-devel >= 2.13}
%{?with_lensfun:Requires:	lensfun-devel >= 0.3.95}
%{?with_libaribcaption:Requires:	libaribcaption-devel}
Requires:	libass-devel >= 0.11.0
%{?with_iec61883:Requires:	libavc1394-devel}
Requires:	libbluray-devel
%{?with_bs2b:Requires:	libbs2b-devel}
%{?with_caca:Requires:	libcaca-devel}
Requires:	libcdio-paranoia-devel >= 0.90-2
%{?with_chromaprint:Requires:	libchromaprint-devel}
%{?with_crystalhd:Requires:	libcrystalhd-devel}
%{?with_dc1394:Requires:	libdc1394-devel >= 2}
%{?with_libdrm:Requires:	libdrm-devel}
%{?with_gsm:Requires:	libgsm-devel}
%{?with_iec61883:Requires:	libiec61883-devel}
%{?with_libjxl:Requires:	libjxl-devel >= 0.7.0}
%{?with_libklvanc:Requires:	libklvanc-devel}
%{?with_modplug:Requires:	libmodplug-devel}
%{?with_libmysofa:Requires:	libmysofa-devel >= 0.7}
%{?with_openmpt:Requires: libopenmpt-devel >= 0.4.5}
%if %{with dc1394} || %{with iec61883}
Requires:	libraw1394-devel >= 2
%endif
%{?with_librist:Requires:	librist-devel >= 0.2.7}
%{?with_librsvg:Requires:	librsvg-devel >= 2}
Requires:	librtmp-devel
%{?with_smb:Requires:	libsmbclient-devel}
%{?with_ssh:Requires:	libssh-devel >= 0.6.0}
Requires:	libstdc++-devel
%{?with_theora:Requires:	libtheora-devel >= 1.0-0.beta3}
Requires:	libv4l-devel
%{?with_va:Requires:	libva-devel >= 1.0.3}
%{?with_va:Requires:	libva-drm-devel >= 1.0.3}
%{?with_va:Requires:	libva-x11-devel >= 1.0.3}
Requires:	libvdpau-devel >= 1.3
Requires:	libvorbis-devel
%{?with_vpl:Requires:	libvpl-devel >= 2.6}
%{?with_vpx:Requires:	libvpx-devel >= 1.4.0}
%{?with_webp:Requires:	libwebp-devel >= 0.4.0}
%{?with_x264:Requires:	libx264-devel >= 0.1.3-1.20130827_2245}
%{?with_x265:Requires:	libx265-devel >= 2.0}
# libxcb xcb-shm xcb-xfixes xcb-shape
Requires:	libxcb-devel >= 1.4
%{?with_libxml2:Requires:	libxml2-devel >= 2}
%{?with_lv2:Requires:	lilv-devel}
%{?with_mfx:Requires:	mfx_dispatch-devel >= 1.28}
%{?with_amr:Requires:	opencore-amr-devel}
%{?with_opencv:Requires:	opencv-devel >= 2}
%{?with_openh264:Requires:	openh264-devel >= 1.3}
Requires:	openjpeg2-devel >= 2.1
Requires:	opus-devel
%{?with_pulseaudio:Requires:	pulseaudio-devel}
%{?with_rabbitmq:Requires:	rabbitmq-c-devel >= 0.7.1}
%{?with_rav1e:Requires:	rav1e-devel >= 0.5.0}
%{?with_rkmpp:Requires:	rockchip-mpp-devel >= 1.3.7}
%{?with_rubberband:Requires:	rubberband-devel >= 1.8.1}
%{?with_shaderc:Requires:	shaderc-devel >= 2019.1}
%{?with_shine:Requires:	shine-devel >= 3.0.0}
%{?with_snappy:Requires:	snappy-devel}
%{?with_soxr:Requires:	soxr-devel}
Requires:	speex-devel >= 1:1.2-rc1
%{?with_glslang:Requires:	spirv-tools-devel}
%{?with_srt:Requires:	srt-devel >= 1.3}
%{?with_svtav1:Requires:	svt-av1-devel >= 0.9.0}
%{?with_tesseract:Requires:	tesseract-devel}
Requires:	twolame-devel >= 0.3.10
%{?with_uavs3d:Requires:	uavs3d-devel >= 1.1.41}
%{?with_vapoursynth:Requires:	vapoursynth-devel >= 42}
%{?with_vidstab:Requires:	vid.stab-devel >= 0.98}
%{?with_voamrwbenc:Requires:	vo-amrwbenc-devel}
%{?with_vmaf:Requires:	vmaf-devel >= 2.0.0}
%{?with_ilbc:Requires:	webrtc-libilbc-devel}
%{?with_avs:Requires:	xavs-devel}
%{?with_avs2:Requires:	xavs2-devel >= 1.3}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXv-devel
%{?with_xvid:Requires:	xvid-devel >= 1:1.1.0}
Requires:	xz-devel
%{?with_zmq:Requires:	zeromq-devel >= 4.2.1}
%{?with_zimg:Requires:	zimg-devel >= 2.7.0}
Requires:	zlib-devel
%{?with_zvbi:Requires:	zvbi-devel >= 0.2.28}
Obsoletes:	libpostproc-devel < 2:1.0-1

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
BuildArch:	noarch

%description doc
FFmpeg documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja pakietu FFmpeg w formacie HTML.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%if %{with v4l2_request}
%patch -P3 -p1
%endif
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1

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
	--extra-cflags="-D_GNU_SOURCE=1 %{rpmcppflags} %{rpmcflags}%{?with_decklink: -I/usr/include/decklink}%{?with_opencv: -I/usr/include/opencv4}" \
	--extra-cxxflags="-D_GNU_SOURCE=1 %{rpmcppflags} %{rpmcxxflags}%{?with_decklink: -I/usr/include/decklink}%{?with_opencv: -I/usr/include/opencv4}" \
	--extra-ldflags="%{rpmcflags} %{rpmldflags}" \
	--cc="%{__cc}" \
	--disable-debug \
	--disable-optimizations \
	--disable-stripping \
	%{!?with_doc:--disable-doc} \
	--enable-avfilter \
	%{?with_avisynth:--enable-avisynth} \
	%{?with_chromaprint:--enable-chromaprint} \
	%{?with_cudasdk:--enable-cuda-nvcc} \
	%{?with_decklink:--enable-decklink} \
	%{!?with_ffnvcodec:--disable-ffnvcodec} \
	--enable-gnutls \
	--enable-gpl \
	--enable-version3 \
	%{?with_frei0r:--enable-frei0r} \
	%{?with_ladspa:--enable-ladspa} \
	%{?with_lcms:--enable-lcms2} \
	%{?with_aom:--enable-libaom} \
	%{?with_aribb24:--enable-libaribb24} \
	%{?with_libaribcaption:--enable-libaribcaption} \
	--enable-libass \
	--enable-libbluray \
	%{?with_bs2b:--enable-libbs2b} \
	%{?with_caca:--enable-libcaca} \
	--enable-libcelt \
	--enable-libcdio \
	%{?with_codec2:--enable-libcodec2} \
	%{?with_dav1d:--enable-libdav1d} \
	%{?with_avs2:--enable-libdavs2} \
	%{?with_dc1394:--enable-libdc1394} \
	%{?with_libdrm:--enable-libdrm} \
	%{?with_flite:--enable-libflite} \
	--enable-libfontconfig \
	--enable-libfreetype \
	%{?with_fribidi:--enable-libfribidi} \
	%{?with_glslang:--enable-libglslang} \
	%{?with_gme:--enable-libgme} \
	%{?with_gsm:--enable-libgsm} \
	--enable-libharfbuzz \
	%{?with_iec61883:--enable-libiec61883} \
	%{?with_ilbc:--enable-libilbc} \
	--enable-libjack \
	%{?with_libjxl:--enable-libjxl} \
	%{?with_kvazaar:--enable-libkvazaar} \
	%{?with_libklvanc:--enable-libklvanc} \
	%{?with_lensfun:--enable-liblensfun} \
	%{?with_mfx:--enable-libmfx} \
	%{?with_modplug:--enable-libmodplug} \
	--enable-libmp3lame \
	%{?with_libmysofa:--enable-libmysofa} \
	%{?with_amr:--enable-libopencore-amrnb} \
	%{?with_amr:--enable-libopencore-amrwb} \
	%{?with_opencv:--enable-libopencv} \
	%{?with_openh264:--enable-libopenh264} \
	--enable-libopenjpeg \
	%{?with_openmpt:--enable-libopenmpt} \
	--enable-libopus \
	%{?with_libplacebo:--enable-libplacebo} \
	%{?with_pulseaudio:--enable-libpulse} \
	%{?with_rabbitmq:--enable-librabbitmq} \
	%{?with_rav1e:--enable-librav1e} \
	%{?with_librist:--enable-librist} \
	%{?with_librsvg:--enable-librsvg} \
	--enable-librtmp \
	%{?with_rubberband:--enable-librubberband} \
	%{?with_shaderc:--enable-libshaderc} \
	%{?with_shine:--enable-libshine} \
	%{?with_smb:--enable-libsmbclient} \
	%{?with_snappy:--enable-libsnappy} \
	%{?with_soxr:--enable-libsoxr} \
	--enable-libspeex \
	%{?with_srt:--enable-libsrt} \
	%{?with_ssh:--enable-libssh} \
	%{?with_svtav1:--enable-libsvtav1} \
	%{?with_tesseract:--enable-libtesseract} \
	%{?with_theora:--enable-libtheora} \
	--enable-libtwolame \
	%{?with_uavs3d:--enable-libuavs3d} \
	--enable-libv4l2 \
	%{?with_vidstab:--enable-libvidstab} \
	%{?with_vmaf:--enable-libvmaf} \
	%{?with_voamrwbenc:--enable-libvo-amrwbenc} \
	--enable-libvorbis \
	%{?with_vpx:--enable-libvpx} \
	%{?with_webp:--enable-libwebp} \
	%{?with_x264:--enable-libx264} \
	%{?with_x265:--enable-libx265} \
	%{?with_avs:--enable-libxavs} \
	%{?with_avs2:--enable-libxavs2} \
	--enable-libxcb \
	%{?with_libxml2:--enable-libxml2} \
	%{?with_xvid:--enable-libxvid} \
	%{?with_zimg:--enable-libzimg} \
	%{?with_zmq:--enable-libzmq} \
	%{?with_zvbi:--enable-libzvbi} \
	%{?with_lv2:--enable-lv2} \
	%{?with_omx:--enable-omx} \
	%{?with_openal:--enable-openal} \
	%{?with_opencl:--enable-opencl} \
	%{?with_opengl:--enable-opengl} \
	%{?with_pocketsphinx:--enable-pocketsphinx} \
	--enable-postproc \
	--enable-pthreads \
	%{?with_rkmpp:--enable-rkmpp} \
	--enable-shared \
	%{!?with_static_libs:--disable-static} \
	--enable-swscale \
	%{!?with_va:--disable-vaapi} \
	%{?with_vapoursynth:--enable-vapoursynth} \
	%{!?with_vulkan:--disable-vulkan} \
%if %{with v4l2_request}
	--enable-libudev \
	--enable-v4l2-request \
%endif
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
%{__rm} $RPM_BUILD_ROOT%{_docdir}/ffmpeg/*.{css,html}
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
%attr(755,root,root) %ghost %{_libdir}/libavcodec.so.60
%attr(755,root,root) %{_libdir}/libavdevice.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavdevice.so.60
%attr(755,root,root) %{_libdir}/libavfilter.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavfilter.so.9
%attr(755,root,root) %{_libdir}/libavformat.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavformat.so.60
%attr(755,root,root) %{_libdir}/libavutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavutil.so.58
%attr(755,root,root) %{_libdir}/libpostproc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpostproc.so.57
%attr(755,root,root) %{_libdir}/libswresample.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libswresample.so.4
%attr(755,root,root) %{_libdir}/libswscale.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libswscale.so.7

%files devel
%defattr(644,root,root,755)
%doc doc/optimization.txt
%attr(755,root,root) %{_bindir}/ffmpeg-avconfig
%attr(755,root,root) %{_libdir}/libavcodec.so
%attr(755,root,root) %{_libdir}/libavdevice.so
%attr(755,root,root) %{_libdir}/libavfilter.so
%attr(755,root,root) %{_libdir}/libavformat.so
%attr(755,root,root) %{_libdir}/libavutil.so
%attr(755,root,root) %{_libdir}/libpostproc.so
%attr(755,root,root) %{_libdir}/libswresample.so
%attr(755,root,root) %{_libdir}/libswscale.so
%{_includedir}/ffmpeg
%{_includedir}/libavcodec
%{_includedir}/libavdevice
%{_includedir}/libavfilter
%{_includedir}/libavformat
%{_includedir}/libavutil
%{_includedir}/libpostproc
%{_includedir}/libswresample
%{_includedir}/libswscale
%{_pkgconfigdir}/libavcodec.pc
%{_pkgconfigdir}/libavdevice.pc
%{_pkgconfigdir}/libavfilter.pc
%{_pkgconfigdir}/libavformat.pc
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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libavcodec.a
%{_libdir}/libavdevice.a
%{_libdir}/libavfilter.a
%{_libdir}/libavformat.a
%{_libdir}/libavutil.a
%{_libdir}/libpostproc.a
%{_libdir}/libswresample.a
%{_libdir}/libswscale.a
%endif

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
%doc doc/*.{css,html}
%endif
