# TODO
# - libnut enabled   no (http://www.nut-container.org/)
#
# Conditional build:
%bcond_with	nonfree		# non free options of package
%bcond_without	autoreqdep	# don't care about package name deps generated by rpm
%bcond_without	imlib2		# don't build imlib2 vhook module

Summary:	FFmpeg is a very fast video and audio converter
Summary(pl.UTF-8):	Koder audio/wideo czasu rzeczywistego oraz serwer strumieni
Name:		ffmpeg
Version:	0.6.1
Release:	1
# LGPL or GPL, chosen at configure time (GPL version is more featured)
# (postprocessing, ac3, xvid, x264, faad)
License:	GPL v3+ with LGPL v3+ parts
Group:		Applications/Multimedia
Source0:	http://ffmpeg.mplayerhq.hu/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	4f5d732d25eedfb072251b5314ba2093
Source1:	ffserver.init
Source2:	ffserver.sysconfig
Source3:	ffserver.conf
Patch0:		%{name}-bug-803.patch
Patch1:		%{name}-gsm.patch
Patch2:		faadbin-libfaadname.patch
# vhook is gone. this patch needs different approach
#PatchX: imagewidth.patch
# http://webm.googlecode.com/files/ffmpeg-0.6_libvpx-0.9.1.diff.gz
Patch3:		ffmpeg-0.6_libvpx-0.9.1.diff
URL:		http://www.ffmpeg.org/
BuildRequires:	SDL-devel
BuildRequires:	dirac-devel >= 1.0.0
BuildRequires:	faac-devel
BuildRequires:	faad2-devel
BuildRequires:	freetype-devel
%ifarch ppc
# require version with altivec support fixed
BuildRequires:	gcc >= 5:3.3.2-3
%endif
%{?with_imlib2:BuildRequires:	imlib2-devel >= 1.3.0}
BuildRequires:	lame-libs-devel
BuildRequires:	libdc1394-devel
BuildRequires:	libgsm-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libtheora-devel >= 1.0-0.beta3
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	libva-devel >= 1.0.3
BuildRequires:	libvdpau-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libvpx-devel >= 0.9.1
# X264_BUILD >= 83
BuildRequires:	libx264-devel >= 0.1.3-1.20100424_2245.1
BuildRequires:	opencore-amr-devel
BuildRequires:	openjpeg-devel >= 1.3-2
BuildRequires:	speex-devel >= 1:1.2-rc1
%ifarch %{ix86}
%ifnarch i386 i486
BuildRequires:	nasm
%endif
%endif
BuildRequires:	perl-Encode
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.470
BuildRequires:	schroedinger-devel
BuildRequires:	tetex
BuildRequires:	texi2html
BuildRequires:	texinfo
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
%define		specflags_ppc	-fPIC

%description
FFmpeg is a complete solution to record, convert and stream audio and
video. It is a command line tool to convert one video file format to
another. It also supports grabbing and encoding in real time from a TV
card.

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
Suggests:	faad2-libs

%description libs
This package contains:
- the codec library from the ffmpeg project. It supports most existing
  encoding formats (MPEG, DivX, MPEG4, AC3, DV...),
- demuxer library from the ffmpeg project. It supports most existing
  file formats (AVI, MPEG, OGG, Matroska, ASF...),
- video postprocessing library from the ffmpeg project.

%description libs -l pl.UTF-8
Ten pakiet zawiera biblioteki współdzielone ffmpeg.

%package devel
Summary:	ffmpeg header files
Summary(pl.UTF-8):	Pliki nagłówkowe ffmpeg
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
# for libavcodec:
Requires:	dirac-devel
Requires:	faac-devel
Requires:	faad2-devel
Requires:	lame-libs-devel
Requires:	libgsm-devel
Requires:	libraw1394-devel
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
%patch1 -p0
%patch2 -p1
%patch3 -p0

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
	--cc="%{__cc}" \
	--extra-cflags="-D_GNU_SOURCE=1 %{rpmcppflags} %{rpmcflags}" \
	--extra-ldflags="%{rpmcflags} %{rpmldflags}" \
	--disable-debug \
	--disable-optimizations \
	--disable-stripping \
	--enable-avfilter \
	--enable-gpl \
	--enable-version3 \
	--enable-libdc1394 \
	--enable-libdirac \
	--enable-libfaad \
	--enable-libfaadbin \
	--enable-libgsm \
	--enable-libmp3lame \
	--enable-libschroedinger \
	--enable-libspeex \
	--enable-libtheora \
	--enable-libvorbis \
	--enable-libvpx \
	--enable-libx264 \
	--enable-libxvid \
	--enable-libopencore-amrnb \
	--enable-libopencore-amrwb \
	--enable-libopenjpeg \
	--enable-postproc \
	--enable-pthreads \
	--enable-shared \
	--enable-swscale \
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
sed -i -e 's|#define.*CONFIG_OLDSCALER.*0|#define CONFIG_OLDSCALER 1|g' config.h

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},/etc/{sysconfig,rc.d/init.d}} \
	$RPM_BUILD_ROOT%{_includedir}/ffmpeg \
	$RPM_BUILD_ROOT/var/{cache,log}/ffserver

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a config.h $RPM_BUILD_ROOT%{_includedir}/ffmpeg
cp -a libavutil/intreadwrite.h $RPM_BUILD_ROOT%{_includedir}/libavutil
cp -a libavutil/bswap.h $RPM_BUILD_ROOT%{_includedir}/libavutil
cp -a libavutil/common.h $RPM_BUILD_ROOT%{_includedir}/libavutil
cp -a libavutil/mem.h $RPM_BUILD_ROOT%{_includedir}/libavutil
for a in libavutil/*/bswap.h; do
	install -D $a $RPM_BUILD_ROOT%{_includedir}/$a
done
cp -a libavformat/riff.h $RPM_BUILD_ROOT%{_includedir}/libavformat
cp -a libavformat/avio.h $RPM_BUILD_ROOT%{_includedir}/libavformat

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ffserver
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/ffserver
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/ffserver.conf
mv -f $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}/ffserver

# install as ffmpeg-avconfig to avoid with possible programs looking for
# ffmpeg-config and expecting --libs output from it which is not implemented
# simple to do (by querying pkgconfig), but why?
install ffmpeg-avconfig $RPM_BUILD_ROOT%{_bindir}/ffmpeg-avconfig

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
%attr(755,root,root) %{_bindir}/ffprobe
%dir %{_datadir}/ffmpeg
%{_datadir}/ffmpeg/*.ffpreset
%{_mandir}/man1/ffmpeg.1*
%{_mandir}/man1/ffprobe.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavcodec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavcodec.so.52
%attr(755,root,root) %{_libdir}/libavdevice.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavdevice.so.52
%attr(755,root,root) %{_libdir}/libavfilter.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavfilter.so.1
%attr(755,root,root) %{_libdir}/libavformat.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavformat.so.52
%attr(755,root,root) %{_libdir}/libavutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavutil.so.50
%attr(755,root,root) %{_libdir}/libpostproc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpostproc.so.51
%attr(755,root,root) %{_libdir}/libswscale.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libswscale.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/optimization.txt
%attr(755,root,root) %{_libdir}/libavcodec.so
%attr(755,root,root) %{_libdir}/libavdevice.so
%attr(755,root,root) %{_libdir}/libavfilter.so
%attr(755,root,root) %{_libdir}/libavformat.so
%attr(755,root,root) %{_libdir}/libavutil.so
%attr(755,root,root) %{_libdir}/libpostproc.so
%attr(755,root,root) %{_libdir}/libswscale.so
%attr(755,root,root) %{_bindir}/ffmpeg-avconfig
%{_includedir}/ffmpeg
%{_includedir}/libavcodec
%{_includedir}/libavdevice
%{_includedir}/libavfilter
%{_includedir}/libavformat
%{_includedir}/libavutil
%{_includedir}/libpostproc
%{_includedir}/libswscale
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files ffplay
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ffplay
%{_mandir}/man1/ffplay.1*

%files ffserver
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ffserver.conf
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/ffserver
%attr(755,root,root) %{_sbindir}/ffserver
%attr(754,root,root) /etc/rc.d/init.d/ffserver
%{_mandir}/man1/ffserver.1*
%dir %attr(770,root,ffserver) /var/cache/ffserver
%dir %attr(770,root,ffserver) /var/log/ffserver
