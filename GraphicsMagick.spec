%define		QuantumDepth	16
%define		pdir		Graphics
%define		pnam		Magick

Summary:	Image display, conversion, and manipulation system
Name:		GraphicsMagick
Version:	1.3.21
Release:	1
License:	MIT
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.graphicsmagick.org/pub/GraphicsMagick/1.3/%{name}-%{version}.tar.xz
# Source0-md5:	f86fe89ea413720a3b04c59c8d5271a2
Patch0:		%{name}-link.patch
URL:		http://www.graphicsmagick.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	expat-devel
BuildRequires:	freetype-devel
BuildRequires:	jasper-devel
BuildRequires:	jbigkit-devel
BuildRequires:	lcms2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libwebp-devel
BuildRequires:	libxml2-devel
BuildRequires:	xorg-libXext-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		modulesdir	%{_libdir}/GraphicsMagick-%{version}/modules-Q%{QuantumDepth}

%description
GraphicsMagick is the swiss army knife of image processing.
It provides a robust and efficient collection of tools and libraries
which support reading, writing, and manipulating an image in over 88
major formats including important formats like DPX, GIF, JPEG,
JPEG-2000, PNG, PDF, PNM, and TIFF.

%package libs
Summary:	GraphicsMagick libraries
Group:		X11/Libraries

%description libs
GraphicsMagick libraries.

%package devel
Summary:	Libraries and header files for GraphicsMagick development
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the GraphicsMagick development package. It includes header
files for use in developing your own applications that make use of the
GraphicsMagick code and/or APIs.

%package coders
Summary:	GraphicsMagick coders
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description coders
GraphicsMagick coders.

%package c++
Summary:	GraphicsMagick Magick++ library
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description c++
This package contains the Magick++ library, a C++ binding to the
GraphicsMagick graphics manipulation library.

%package c++-devel
Summary:	C++ bindings for the GraphicsMagick library
Group:		X11/Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description c++-devel
GraphicsMagick-c++-devel contains header files you'll need to develop
GraphicsMagick applications using the Magick++ C++ bindings.
GraphicsMagick is an image manipulation program.

%package perl
Summary:	Libraries and modules for access to GraphicsMagick from Perl
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}

%description perl
This is the GraphicsMagick Perl support package. It perl modules and
support files for access to GraphicsMagick library from perl without
unuseful forking or such.

%package doc
Summary:	GraphicsMagick documentation
Group:		Documentation

%description doc
Documentation for GraphicsMagick.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-ltdl-install			\
	--disable-static			\
	--enable-fast-install			\
	--enable-shared				\
	--with-gs-font-dir=%{_fontsdir}/Type1	\
	--with-jp2				\
	--with-magick_plus_plus			\
	--with-modules				\
	--with-perl-options="INSTALLDIRS=vendor" \
	--with-perl=%{__perl}			\
	--with-quantum-depth=%{QuantumDepth}	\
	--with-threads				\
	--with-ttf				\
	--with-x				\
	--without-dps				\
	--without-fpx				\
	--without-gslib
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgdocdir=%{_docdir}/%{name}-devel-%{version}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /usr/sbin/ldconfig
%postun libs -p /usr/sbin/ldconfig

%post   c++ -p /usr/sbin/ldconfig
%postun c++ -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gm

%dir %{_datadir}/GraphicsMagick-%{version}
%dir %{_datadir}/GraphicsMagick-%{version}/config
%dir %{_libdir}/GraphicsMagick-%{version}
%dir %{_libdir}/GraphicsMagick-%{version}/config

%{_datadir}/GraphicsMagick-%{version}/config/*.mgk
%{_libdir}/GraphicsMagick-%{version}/config/*.mgk
%{_mandir}/man1/gm.1*
%{_mandir}/man4/miff.4*

%dir %{modulesdir}
%dir %{modulesdir}/coders

%attr(755,root,root) %{modulesdir}/coders/art.so
%attr(755,root,root) %{modulesdir}/coders/avs.so
%attr(755,root,root) %{modulesdir}/coders/bmp.so
%attr(755,root,root) %{modulesdir}/coders/cals.so
%attr(755,root,root) %{modulesdir}/coders/caption.so
%attr(755,root,root) %{modulesdir}/coders/cineon.so
%attr(755,root,root) %{modulesdir}/coders/cmyk.so
%attr(755,root,root) %{modulesdir}/coders/cut.so
%attr(755,root,root) %{modulesdir}/coders/dcm.so
%attr(755,root,root) %{modulesdir}/coders/dcraw.so
%attr(755,root,root) %{modulesdir}/coders/dib.so
%attr(755,root,root) %{modulesdir}/coders/dpx.so
%attr(755,root,root) %{modulesdir}/coders/ept.so
%attr(755,root,root) %{modulesdir}/coders/fax.so
%attr(755,root,root) %{modulesdir}/coders/fits.so
%attr(755,root,root) %{modulesdir}/coders/gif.so
%attr(755,root,root) %{modulesdir}/coders/gradient.so
%attr(755,root,root) %{modulesdir}/coders/gray.so
%attr(755,root,root) %{modulesdir}/coders/histogram.so
%attr(755,root,root) %{modulesdir}/coders/hrz.so
%attr(755,root,root) %{modulesdir}/coders/html.so
%attr(755,root,root) %{modulesdir}/coders/icon.so
%attr(755,root,root) %{modulesdir}/coders/identity.so
%attr(755,root,root) %{modulesdir}/coders/info.so
%attr(755,root,root) %{modulesdir}/coders/jnx.so
%attr(755,root,root) %{modulesdir}/coders/label.so
%attr(755,root,root) %{modulesdir}/coders/locale.so
%attr(755,root,root) %{modulesdir}/coders/logo.so
%attr(755,root,root) %{modulesdir}/coders/mac.so
%attr(755,root,root) %{modulesdir}/coders/map.so
%attr(755,root,root) %{modulesdir}/coders/mat.so
%attr(755,root,root) %{modulesdir}/coders/matte.so
%attr(755,root,root) %{modulesdir}/coders/meta.so
%attr(755,root,root) %{modulesdir}/coders/mono.so
%attr(755,root,root) %{modulesdir}/coders/mpc.so
%attr(755,root,root) %{modulesdir}/coders/mpeg.so
%attr(755,root,root) %{modulesdir}/coders/mtv.so
%attr(755,root,root) %{modulesdir}/coders/mvg.so
%attr(755,root,root) %{modulesdir}/coders/null.so
%attr(755,root,root) %{modulesdir}/coders/otb.so
%attr(755,root,root) %{modulesdir}/coders/palm.so
%attr(755,root,root) %{modulesdir}/coders/pcd.so
%attr(755,root,root) %{modulesdir}/coders/pcl.so
%attr(755,root,root) %{modulesdir}/coders/pcx.so
%attr(755,root,root) %{modulesdir}/coders/pdb.so
%attr(755,root,root) %{modulesdir}/coders/pict.so
%attr(755,root,root) %{modulesdir}/coders/pix.so
%attr(755,root,root) %{modulesdir}/coders/plasma.so
%attr(755,root,root) %{modulesdir}/coders/pnm.so
%attr(755,root,root) %{modulesdir}/coders/preview.so
%attr(755,root,root) %{modulesdir}/coders/ps.so
%attr(755,root,root) %{modulesdir}/coders/psd.so
%attr(755,root,root) %{modulesdir}/coders/pwp.so
%attr(755,root,root) %{modulesdir}/coders/rgb.so
%attr(755,root,root) %{modulesdir}/coders/rla.so
%attr(755,root,root) %{modulesdir}/coders/rle.so
%attr(755,root,root) %{modulesdir}/coders/sct.so
%attr(755,root,root) %{modulesdir}/coders/sfw.so
%attr(755,root,root) %{modulesdir}/coders/sgi.so
%attr(755,root,root) %{modulesdir}/coders/stegano.so
%attr(755,root,root) %{modulesdir}/coders/sun.so
%attr(755,root,root) %{modulesdir}/coders/tga.so
%attr(755,root,root) %{modulesdir}/coders/tile.so
%attr(755,root,root) %{modulesdir}/coders/tim.so
%attr(755,root,root) %{modulesdir}/coders/topol.so
%attr(755,root,root) %{modulesdir}/coders/ttf.so
%attr(755,root,root) %{modulesdir}/coders/txt.so
%attr(755,root,root) %{modulesdir}/coders/uil.so
%attr(755,root,root) %{modulesdir}/coders/uyvy.so
%attr(755,root,root) %{modulesdir}/coders/vicar.so
%attr(755,root,root) %{modulesdir}/coders/vid.so
%attr(755,root,root) %{modulesdir}/coders/viff.so
%attr(755,root,root) %{modulesdir}/coders/wbmp.so
%attr(755,root,root) %{modulesdir}/coders/wpg.so
%attr(755,root,root) %{modulesdir}/coders/x.so
%attr(755,root,root) %{modulesdir}/coders/xbm.so
%attr(755,root,root) %{modulesdir}/coders/xc.so
%attr(755,root,root) %{modulesdir}/coders/xcf.so
%attr(755,root,root) %{modulesdir}/coders/xpm.so
%attr(755,root,root) %{modulesdir}/coders/xwd.so
%attr(755,root,root) %{modulesdir}/coders/yuv.so
%{modulesdir}/coders/art.la
%{modulesdir}/coders/avs.la
%{modulesdir}/coders/bmp.la
%{modulesdir}/coders/cals.la
%{modulesdir}/coders/caption.la
%{modulesdir}/coders/cineon.la
%{modulesdir}/coders/cmyk.la
%{modulesdir}/coders/cut.la
%{modulesdir}/coders/dcm.la
%{modulesdir}/coders/dcraw.la
%{modulesdir}/coders/dib.la
%{modulesdir}/coders/dpx.la
%{modulesdir}/coders/ept.la
%{modulesdir}/coders/fax.la
%{modulesdir}/coders/fits.la
%{modulesdir}/coders/gif.la
%{modulesdir}/coders/gradient.la
%{modulesdir}/coders/gray.la
%{modulesdir}/coders/histogram.la
%{modulesdir}/coders/hrz.la
%{modulesdir}/coders/html.la
%{modulesdir}/coders/icon.la
%{modulesdir}/coders/identity.la
%{modulesdir}/coders/info.la
%{modulesdir}/coders/jnx.la
%{modulesdir}/coders/label.la
%{modulesdir}/coders/locale.la
%{modulesdir}/coders/logo.la
%{modulesdir}/coders/mac.la
%{modulesdir}/coders/map.la
%{modulesdir}/coders/mat.la
%{modulesdir}/coders/matte.la
%{modulesdir}/coders/meta.la
%{modulesdir}/coders/mono.la
%{modulesdir}/coders/mpc.la
%{modulesdir}/coders/mpeg.la
%{modulesdir}/coders/mtv.la
%{modulesdir}/coders/mvg.la
%{modulesdir}/coders/null.la
%{modulesdir}/coders/otb.la
%{modulesdir}/coders/palm.la
%{modulesdir}/coders/pcd.la
%{modulesdir}/coders/pcl.la
%{modulesdir}/coders/pcx.la
%{modulesdir}/coders/pdb.la
%{modulesdir}/coders/pict.la
%{modulesdir}/coders/pix.la
%{modulesdir}/coders/plasma.la
%{modulesdir}/coders/pnm.la
%{modulesdir}/coders/preview.la
%{modulesdir}/coders/ps.la
%{modulesdir}/coders/psd.la
%{modulesdir}/coders/pwp.la
%{modulesdir}/coders/rgb.la
%{modulesdir}/coders/rla.la
%{modulesdir}/coders/rle.la
%{modulesdir}/coders/sct.la
%{modulesdir}/coders/sfw.la
%{modulesdir}/coders/sgi.la
%{modulesdir}/coders/stegano.la
%{modulesdir}/coders/sun.la
%{modulesdir}/coders/tga.la
%{modulesdir}/coders/tile.la
%{modulesdir}/coders/tim.la
%{modulesdir}/coders/topol.la
%{modulesdir}/coders/ttf.la
%{modulesdir}/coders/txt.la
%{modulesdir}/coders/uil.la
%{modulesdir}/coders/uyvy.la
%{modulesdir}/coders/vicar.la
%{modulesdir}/coders/vid.la
%{modulesdir}/coders/viff.la
%{modulesdir}/coders/wbmp.la
%{modulesdir}/coders/wpg.la
%{modulesdir}/coders/x.la
%{modulesdir}/coders/xbm.la
%{modulesdir}/coders/xc.la
%{modulesdir}/coders/xcf.la
%{modulesdir}/coders/xpm.la
%{modulesdir}/coders/xwd.la
%{modulesdir}/coders/yuv.la
%dir %{modulesdir}/filters
%attr(755,root,root) %{modulesdir}/filters/analyze.so
%{modulesdir}/filters/analyze.la

%files libs
%defattr(644,root,root,755)
%doc ChangeLog Copyright.txt NEWS.txt README.txt TODO.txt
%attr(755,root,root) %ghost %{_libdir}/libGraphicsMagick.so.3
%attr(755,root,root) %ghost %{_libdir}/libGraphicsMagickWand.so.2
%attr(755,root,root) %{_libdir}/libGraphicsMagick.so.*.*.*
%attr(755,root,root) %{_libdir}/libGraphicsMagickWand.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/GraphicsMagick-config
%attr(755,root,root) %{_bindir}/GraphicsMagickWand-config
%attr(755,root,root) %{_libdir}/libGraphicsMagick.so
%attr(755,root,root) %{_libdir}/libGraphicsMagickWand.so

%dir %{_includedir}/GraphicsMagick
%doc %{_docdir}/%{name}

%{_includedir}/GraphicsMagick/magick
%{_includedir}/GraphicsMagick/wand
%{_pkgconfigdir}/GraphicsMagick.pc
%{_pkgconfigdir}/GraphicsMagickWand.pc

%{_mandir}/man1/GraphicsMagick-config.1*
%{_mandir}/man1/GraphicsMagickWand-config.1*
%{_mandir}/man5/quantize.5*

%files coders
%defattr(644,root,root,755)
%attr(755,root,root) %{modulesdir}/coders/jbig.so
%attr(755,root,root) %{modulesdir}/coders/jp2.so
%attr(755,root,root) %{modulesdir}/coders/jpeg.so
%attr(755,root,root) %{modulesdir}/coders/miff.so
%attr(755,root,root) %{modulesdir}/coders/mpr.so
%attr(755,root,root) %{modulesdir}/coders/msl.so
%attr(755,root,root) %{modulesdir}/coders/pdf.so
%attr(755,root,root) %{modulesdir}/coders/png.so
%attr(755,root,root) %{modulesdir}/coders/ps2.so
%attr(755,root,root) %{modulesdir}/coders/ps3.so
%attr(755,root,root) %{modulesdir}/coders/svg.so
%attr(755,root,root) %{modulesdir}/coders/tiff.so
%attr(755,root,root) %{modulesdir}/coders/url.so
%attr(755,root,root) %{modulesdir}/coders/webp.so
%attr(755,root,root) %{modulesdir}/coders/wmf.so
%{modulesdir}/coders/jbig.la
%{modulesdir}/coders/jp2.la
%{modulesdir}/coders/jpeg.la
%{modulesdir}/coders/miff.la
%{modulesdir}/coders/mpr.la
%{modulesdir}/coders/msl.la
%{modulesdir}/coders/pdf.la
%{modulesdir}/coders/png.la
%{modulesdir}/coders/ps2.la
%{modulesdir}/coders/ps3.la
%{modulesdir}/coders/svg.la
%{modulesdir}/coders/tiff.la
%{modulesdir}/coders/url.la
%{modulesdir}/coders/webp.la
%{modulesdir}/coders/wmf.la

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGraphicsMagick++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libGraphicsMagick++.so.11

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/GraphicsMagick++-config
%attr(755,root,root) %{_libdir}/libGraphicsMagick++.so
%{_includedir}/GraphicsMagick/Magick++
%{_includedir}/GraphicsMagick/Magick++.h
%{_pkgconfigdir}/GraphicsMagick++.pc
%{_mandir}/man1/GraphicsMagick++-config.1*

%files doc
%defattr(644,root,root,755)
%doc www

