#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : MuseScore
Version  : 3.2.2
Release  : 5
URL      : https://github.com/musescore/MuseScore/archive/v3.2.2/MuseScore-3.2.2.tar.gz
Source0  : https://github.com/musescore/MuseScore/archive/v3.2.2/MuseScore-3.2.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC-BY-4.0 FTL GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT OpenSSL
Requires: MuseScore-bin = %{version}-%{release}
Requires: MuseScore-data = %{version}-%{release}
Requires: MuseScore-license = %{version}-%{release}
Requires: MuseScore-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : freetype-dev
BuildRequires : libsndfile-dev
BuildRequires : libvorbis-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(harfbuzz-icu)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(portaudio-2.0)
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtsvg-dev
BuildRequires : qttools-dev
BuildRequires : qtwebengine-dev
BuildRequires : qtxmlpatterns-dev

%description
References
* Cakewalk® Synthesizers: From Presets to Power User, Second Edition
Simon Cann - Course Technology - 2009

%package bin
Summary: bin components for the MuseScore package.
Group: Binaries
Requires: MuseScore-data = %{version}-%{release}
Requires: MuseScore-license = %{version}-%{release}

%description bin
bin components for the MuseScore package.


%package data
Summary: data components for the MuseScore package.
Group: Data

%description data
data components for the MuseScore package.


%package license
Summary: license components for the MuseScore package.
Group: Default

%description license
license components for the MuseScore package.


%package man
Summary: man components for the MuseScore package.
Group: Default

%description man
man components for the MuseScore package.


%prep
%setup -q -n MuseScore-3.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1562011629
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DBUILD_WEBENGINE=OFF \
-DUSE_SYSTEM_FREETYPE=ON \
-DBUILD_LAME=OFF \
-DBUILD_JACK=OFF \
-DBUILD_PORTMIDI=OFF \
-DBUILD_PCH=OFF \
-DBUILD_AUTOUPDATE=OFF \
-DBUILD_CRASH_REPORTER=OFF
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1562011629
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/MuseScore
cp LICENSE.GPL %{buildroot}/usr/share/package-licenses/MuseScore/LICENSE.GPL
cp LICENSE.rtf %{buildroot}/usr/share/package-licenses/MuseScore/LICENSE.rtf
cp aeolus/COPYING %{buildroot}/usr/share/package-licenses/MuseScore/aeolus_COPYING
cp bww2mxml/COPYING %{buildroot}/usr/share/package-licenses/MuseScore/bww2mxml_COPYING
cp effects/chorus/COPYING %{buildroot}/usr/share/package-licenses/MuseScore/effects_chorus_COPYING
cp mscore/data/icons/LICENSE.md %{buildroot}/usr/share/package-licenses/MuseScore/mscore_data_icons_LICENSE.md
cp mscore/licence.h %{buildroot}/usr/share/package-licenses/MuseScore/mscore_licence.h
cp share/wallpaper/COPYRIGHT %{buildroot}/usr/share/package-licenses/MuseScore/share_wallpaper_COPYRIGHT
cp thirdparty/beatroot/COPYING %{buildroot}/usr/share/package-licenses/MuseScore/thirdparty_beatroot_COPYING
cp thirdparty/dtl/COPYING %{buildroot}/usr/share/package-licenses/MuseScore/thirdparty_dtl_COPYING
cp thirdparty/freetype/docs/GPLv2.TXT %{buildroot}/usr/share/package-licenses/MuseScore/thirdparty_freetype_docs_GPLv2.TXT
cp thirdparty/freetype/docs/LICENSE.TXT %{buildroot}/usr/share/package-licenses/MuseScore/thirdparty_freetype_docs_LICENSE.TXT
cp thirdparty/intervaltree/LICENSE %{buildroot}/usr/share/package-licenses/MuseScore/thirdparty_intervaltree_LICENSE
cp thirdparty/kQOAuth/COPYING %{buildroot}/usr/share/package-licenses/MuseScore/thirdparty_kQOAuth_COPYING
cp thirdparty/openssl/LICENSE %{buildroot}/usr/share/package-licenses/MuseScore/thirdparty_openssl_LICENSE
cp thirdparty/portmidi/license.txt %{buildroot}/usr/share/package-licenses/MuseScore/thirdparty_portmidi_license.txt
cp thirdparty/rtf2html/COPYING.LESSER %{buildroot}/usr/share/package-licenses/MuseScore/thirdparty_rtf2html_COPYING.LESSER
cp thirdparty/singleapp/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/MuseScore/thirdparty_singleapp_LICENSE.GPL3
cp thirdparty/singleapp/LICENSE.LGPL %{buildroot}/usr/share/package-licenses/MuseScore/thirdparty_singleapp_LICENSE.LGPL
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mscore
/usr/bin/musescore

%files data
%defattr(-,root,root,-)
/usr/share/applications/mscore.desktop
/usr/share/icons/hicolor/128x128/apps/mscore.png
/usr/share/icons/hicolor/16x16/apps/mscore.png
/usr/share/icons/hicolor/24x24/apps/mscore.png
/usr/share/icons/hicolor/32x32/apps/mscore.png
/usr/share/icons/hicolor/48x48/apps/mscore.png
/usr/share/icons/hicolor/48x48/mimetypes/application-vnd.recordare.musicxml+xml.png
/usr/share/icons/hicolor/48x48/mimetypes/application-vnd.recordare.musicxml.png
/usr/share/icons/hicolor/48x48/mimetypes/application-x-musescore+xml.png
/usr/share/icons/hicolor/48x48/mimetypes/application-x-musescore.png
/usr/share/icons/hicolor/512x512/apps/mscore.png
/usr/share/icons/hicolor/64x64/apps/mscore.png
/usr/share/icons/hicolor/96x96/apps/mscore.png
/usr/share/icons/hicolor/scalable/apps/mscore.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-vnd.recordare.musicxml+xml.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-vnd.recordare.musicxml.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-x-musescore+xml.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-x-musescore.svg
/usr/share/metainfo/org.musescore.MuseScore.appdata.xml
/usr/share/mime-packages/musescore.xml
/usr/share/mscore-3.2/demos/Brassed_Up.mscx
/usr/share/mscore-3.2/demos/Dynamic_Strings.mscx
/usr/share/mscore-3.2/demos/Fugue_1.mscx
/usr/share/mscore-3.2/demos/Reunion.mscz
/usr/share/mscore-3.2/demos/Unclaimed_Gift.mscx
/usr/share/mscore-3.2/instruments/instruments.xml
/usr/share/mscore-3.2/locale/languages.xml
/usr/share/mscore-3.2/manual/plugins/manual.css
/usr/share/mscore-3.2/manual/plugins/plugins3.html
/usr/share/mscore-3.2/plugins/abc_import.qml
/usr/share/mscore-3.2/plugins/colornotes.qml
/usr/share/mscore-3.2/plugins/createscore.qml
/usr/share/mscore-3.2/plugins/helloqml/helloqml.qml
/usr/share/mscore-3.2/plugins/helloqml/translations/locale_de.qm
/usr/share/mscore-3.2/plugins/helloqml/translations/locale_de.ts
/usr/share/mscore-3.2/plugins/notenames.qml
/usr/share/mscore-3.2/plugins/panel.qml
/usr/share/mscore-3.2/plugins/random.qml
/usr/share/mscore-3.2/plugins/random2.qml
/usr/share/mscore-3.2/plugins/run.qml
/usr/share/mscore-3.2/plugins/scorelist.qml
/usr/share/mscore-3.2/plugins/view.qml
/usr/share/mscore-3.2/plugins/walk.qml
/usr/share/mscore-3.2/sound/MuseScore_General-License.md
/usr/share/mscore-3.2/sound/MuseScore_General.sf3
/usr/share/mscore-3.2/styles/MuseJazz.mss
/usr/share/mscore-3.2/styles/cchords_muse.xml
/usr/share/mscore-3.2/styles/cchords_nrb.xml
/usr/share/mscore-3.2/styles/cchords_rb.xml
/usr/share/mscore-3.2/styles/cchords_sym.xml
/usr/share/mscore-3.2/styles/chords.xml
/usr/share/mscore-3.2/styles/chords_jazz.xml
/usr/share/mscore-3.2/styles/chords_std.xml
/usr/share/mscore-3.2/styles/jazzchords.xml
/usr/share/mscore-3.2/styles/stdchords.xml
/usr/share/mscore-3.2/templates/01-General/00-Blank.mscx
/usr/share/mscore-3.2/templates/01-General/01-Treble_Clef.mscx
/usr/share/mscore-3.2/templates/01-General/02-Bass_Clef.mscx
/usr/share/mscore-3.2/templates/01-General/03-Grand_Staff.mscx
/usr/share/mscore-3.2/templates/02-Choral/01-SATB.mscx
/usr/share/mscore-3.2/templates/02-Choral/02-SATB_+_Organ.mscx
/usr/share/mscore-3.2/templates/02-Choral/03-SATB_+_Piano.mscx
/usr/share/mscore-3.2/templates/02-Choral/04-SATB_Closed_Score.mscx
/usr/share/mscore-3.2/templates/02-Choral/05-SATB_Closed_Score_+_Organ.mscx
/usr/share/mscore-3.2/templates/02-Choral/06-SATB_Closed_Score_+_Piano.mscx
/usr/share/mscore-3.2/templates/02-Choral/07-Voice_+_Piano.mscx
/usr/share/mscore-3.2/templates/02-Choral/08-Barbershop_Quartet.mscx
/usr/share/mscore-3.2/templates/02-Choral/09-Liturgical_Unmetrical.mscx
/usr/share/mscore-3.2/templates/02-Choral/10-Liturgical_Unmetrical_+_Organ.mscx
/usr/share/mscore-3.2/templates/03-Chamber_Music/01-String_Quartet.mscx
/usr/share/mscore-3.2/templates/03-Chamber_Music/02-Wind_Quartet.mscx
/usr/share/mscore-3.2/templates/03-Chamber_Music/03-Wind_Quintet.mscx
/usr/share/mscore-3.2/templates/03-Chamber_Music/04-Saxophone_Quartet.mscx
/usr/share/mscore-3.2/templates/03-Chamber_Music/05-Brass_Quartet.mscx
/usr/share/mscore-3.2/templates/03-Chamber_Music/06-Brass_Quintet.mscx
/usr/share/mscore-3.2/templates/04-Solo/01-Guitar.mscx
/usr/share/mscore-3.2/templates/04-Solo/02-Guitar_+_Tablature.mscx
/usr/share/mscore-3.2/templates/04-Solo/03-Guitar_Tablature.mscx
/usr/share/mscore-3.2/templates/04-Solo/04-Piano.mscx
/usr/share/mscore-3.2/templates/05-Jazz/01-Jazz_Lead_Sheet.mscx
/usr/share/mscore-3.2/templates/05-Jazz/02-Big_Band.mscx
/usr/share/mscore-3.2/templates/05-Jazz/03-Jazz_Combo.mscx
/usr/share/mscore-3.2/templates/06-Popular/01-Rock_Band.mscx
/usr/share/mscore-3.2/templates/06-Popular/02-Bluegrass_Band.mscx
/usr/share/mscore-3.2/templates/07-Band_and_Percussion/01-Concert_Band.mscx
/usr/share/mscore-3.2/templates/07-Band_and_Percussion/02-Small_Concert_Band.mscx
/usr/share/mscore-3.2/templates/07-Band_and_Percussion/03-Brass_Band.mscx
/usr/share/mscore-3.2/templates/07-Band_and_Percussion/04-Marching_Band.mscx
/usr/share/mscore-3.2/templates/07-Band_and_Percussion/05-Small_Marching_Band.mscx
/usr/share/mscore-3.2/templates/07-Band_and_Percussion/06-Battery_Percussion.mscx
/usr/share/mscore-3.2/templates/07-Band_and_Percussion/07-Large_Pit_Percussion.mscx
/usr/share/mscore-3.2/templates/07-Band_and_Percussion/08-Small_Pit_Percussion.mscx
/usr/share/mscore-3.2/templates/07-Band_and_Percussion/09-European_Concert_Band.mscx
/usr/share/mscore-3.2/templates/08-Orchestral/01-Classical_Orchestra.mscx
/usr/share/mscore-3.2/templates/08-Orchestral/02-Symphony_Orchestra.mscx
/usr/share/mscore-3.2/templates/08-Orchestral/03-String_Orchestra.mscx
/usr/share/mscore-3.2/templates/drumset_fr.drm
/usr/share/mscore-3.2/templates/orchestral.drm
/usr/share/mscore-3.2/tours/autoplace.tour
/usr/share/mscore-3.2/tours/inspector.tour
/usr/share/mscore-3.2/tours/mmrest.tour
/usr/share/mscore-3.2/tours/navigate.tour
/usr/share/mscore-3.2/tours/noteinput.tour
/usr/share/mscore-3.2/tours/palette.tour
/usr/share/mscore-3.2/tours/select.tour
/usr/share/mscore-3.2/tours/spanner-drop-apply.tour
/usr/share/mscore-3.2/tours/timeline.tour
/usr/share/mscore-3.2/tours/welcome.tour
/usr/share/mscore-3.2/wallpaper/background1.png
/usr/share/mscore-3.2/wallpaper/paper1.png
/usr/share/mscore-3.2/wallpaper/paper2.png
/usr/share/mscore-3.2/wallpaper/paper3.png
/usr/share/mscore-3.2/wallpaper/paper4.png
/usr/share/mscore-3.2/wallpaper/paper5.png
/usr/share/mscore-3.2/wallpaper/paper6.png
/usr/share/mscore-3.2/wallpaper/paper7.png
/usr/share/mscore-3.2/workspaces/Advanced.workspace
/usr/share/mscore-3.2/workspaces/Basic.workspace

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/MuseScore/LICENSE.GPL
/usr/share/package-licenses/MuseScore/LICENSE.rtf
/usr/share/package-licenses/MuseScore/aeolus_COPYING
/usr/share/package-licenses/MuseScore/bww2mxml_COPYING
/usr/share/package-licenses/MuseScore/effects_chorus_COPYING
/usr/share/package-licenses/MuseScore/mscore_data_icons_LICENSE.md
/usr/share/package-licenses/MuseScore/mscore_licence.h
/usr/share/package-licenses/MuseScore/share_wallpaper_COPYRIGHT
/usr/share/package-licenses/MuseScore/thirdparty_beatroot_COPYING
/usr/share/package-licenses/MuseScore/thirdparty_dtl_COPYING
/usr/share/package-licenses/MuseScore/thirdparty_freetype_docs_GPLv2.TXT
/usr/share/package-licenses/MuseScore/thirdparty_freetype_docs_LICENSE.TXT
/usr/share/package-licenses/MuseScore/thirdparty_intervaltree_LICENSE
/usr/share/package-licenses/MuseScore/thirdparty_kQOAuth_COPYING
/usr/share/package-licenses/MuseScore/thirdparty_openssl_LICENSE
/usr/share/package-licenses/MuseScore/thirdparty_portmidi_license.txt
/usr/share/package-licenses/MuseScore/thirdparty_rtf2html_COPYING.LESSER
/usr/share/package-licenses/MuseScore/thirdparty_singleapp_LICENSE.GPL3
/usr/share/package-licenses/MuseScore/thirdparty_singleapp_LICENSE.LGPL

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mscore.1.gz
/usr/share/man/man1/musescore.1.gz
