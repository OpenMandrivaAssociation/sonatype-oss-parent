%global artifactid oss-parent

Name:           sonatype-oss-parent
Version:        6
Release:        2
Summary:        Sonatype OSS Parent

Group:          Development/Java
License:        ASL 2.0
URL:            http://svn.sonatype.org/spice/tags/oss-parent-6
#svn export http://svn.sonatype.org/spice/tags/oss-parent-6 sonatype-oss-parent-6
#tar zcf sonatype-oss-parent-6.tar.gz sonatype-oss-parent-6/
Source0:       %{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires:  jpackage-utils >= 0:1.7.2

Requires:          jpackage-utils
Requires:          maven-release-plugin
Requires(post):    jpackage-utils >= 0:1.7.2
Requires(postun):  jpackage-utils >= 0:1.7.2

%description
Sonatype OSS parent pom used by other sonatype packages

%prep
%setup -q -n %{name}-%{version}

%build
#nothing to do for the pom

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_to_maven_depmap org.sonatype.oss %{artifactid} %{version} JPP %{name}

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(-,root,root,-)
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

