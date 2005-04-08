#
# Conditional build:
%bcond_without	imlib2		# we can safely play without it :-)
%bcond_without	broken_rpm	# dont BC packages because of logic error in Ac
#
Summary:	Realtime audio/video encoder and streaming server
Summary(pl):	Koder audio/wideo czasu rzeczywistego oraz serwer strumieni
Name:		ffmpeg
Version:	0.4.9
Release:	0.pre1.1
# LGPL or GPL, chosen at configure time (GPL version is more featured)
License:	GPL
Group:		Daemons
Source0:	http://dl.sourceforge.net/ffmpeg/%{name}-%{version}-pre1.tar.gz
# Source0-md5:	ea5587e3c66d50b1503b82ac4179c303
Patch0:		%{name}-imlib2.patch
Patch1:		%{name}-libtool.patch
URL:		http://ffmpeg.sourceforge.net/
%if %{with broken_rpm}
BuildConflicts:	libpostproc
%endif
BuildRequires:	SDL-devel
BuildRequires:	freetype-devel
%ifarch ppc
# require version with altivec support fixed
BuildRequires:	gcc >= 5:3.3.2-3
%endif
%{?with_imlib2:BuildRequires:	imlib2-devel >= 1.1.0-2}
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:  faac-devel
%ifarch %{ix86}
%ifnarch i386 i486
BuildRequires:	nasm
%endif
%endif
BuildRequires:	perl-tools-pod
BuildRequires:	tetex
BuildRequires:	texinfo
BuildRequires:	zlib-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libvorbis-devel
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
%setup -q -n ffmpeg-0.4.9-pre1
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
	--enable-a52bin \
	--enable-faac \
	--enable-faadbin \
	--enable-pthreads \
	--enable-gpl \
	--enable-pp \
	--enable-shared \
	--enable-shared-pp \
	--enable-mp3lame \
	--enable-vorbis \
%ifnarch %{ix86}
	--disable-mmx \
%endif
%ifarch i386 i486
	--disable-mmx \
%endif
	--cc="%{__cc}" \
	--extra-cflags="%{rpmcflags} -fomit-frame-pointer" \
	--extra-ldflags="%{rpmldflags}" \
	--disable-debug \
	--disable-opts \
	--tune=generic

%{__make} \
	BUILD_DOC=yes

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
%attr(755,root,root) %{_bindir}/ffmpeg
%attr(755,root,root) %{_sbindir}/ffserver
%attr(755,root,root) %{_libdir}/libavcodec-*.so
%attr(755,root,root) %{_libdir}/libavformat-*.so
%attr(755,root,root) %{_libdir}/libpostproc.so.*
%dir %{_libdir}/vhook
%attr(755,root,root) %{_libdir}/vhook/drawtext.so
%attr(755,root,root) %{_libdir}/vhook/fish.so
%attr(755,root,root) %{_libdir}/vhook/null.so
%attr(755,root,root) %{_libdir}/vhook/ppm.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ffserver.conf
%{_mandir}/man1/ffmpeg.1*
%{_mandir}/man1/ffserver.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavcodec.so
%attr(755,root,root) %{_libdir}/libavformat.so
%attr(755,root,root) %{_libdir}/libpostproc.so
%{_libdir}/lib*.la
%{_includedir}/ffmpeg
%{_includedir}/postproc

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
