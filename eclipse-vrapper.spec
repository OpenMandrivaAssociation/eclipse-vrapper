%global svnrev      351
%global eclipse_base        %{_libdir}/eclipse

Name:           eclipse-vrapper
Version:        0.15.0
Release:        0.3.svn%{svnrev}
Summary:        Vim-like editing in Eclipse

Group:          Development/Java
License:        GPLv3+
URL:            https://vrapper.sourceforge.net
Source0:        vrapper-%{version}-r%{svnrev}.tar.bz2
# Source gathered via:
# svn co -r r351 https://vrapper.svn.sourceforge.net/svnroot/vrapper vrapper-0.15.0
# tar cjvpf vrapper-0.15.0-r351.tar.bz2 vrapper-0.15.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  java-devel >= 1.5.0
BuildRequires:  eclipse-pde
Requires:       eclipse-platform

%description
Vrapper is an eclipse plugin which acts as a wrapper for eclipse text editors
to provide a Vim-like input scheme for moving around and editing text.

%prep
%setup -q -n vrapper-%{version}

%build
pushd trunk
%{eclipse_base}/buildscripts/pdebuild -f net.sourceforge.vrapper
%{eclipse_base}/buildscripts/pdebuild -f net.sourceforge.vrapper.plugin.surround
popd

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/eclipse/dropins/vrapper
unzip -q -d $RPM_BUILD_ROOT%{_datadir}/eclipse/dropins/vrapper \
trunk/build/rpmBuild/net.sourceforge.vrapper.zip
unzip -q -d $RPM_BUILD_ROOT%{_datadir}/eclipse/dropins/vrapper \
trunk/build/rpmBuild/net.sourceforge.vrapper.plugin.surround.zip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/eclipse/dropins/vrapper

