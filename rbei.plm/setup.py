from cdb.comparch.pkgtools import setup

setup(
    name="rbei.plm",
    version="1.0.0",
    install_requires=['cs.actions', 'cs.activitystream', 'cs.base', 'cs.bomcreator', 'cs.classification', 'cs.costing', 'cs.cp', 'cs.defects', 'cs.designsystem', 'cs.documents', 'cs.dsig', 'cs.dsig-pdf', 'cs.ec', 'cs.innovation', 'cs.launchpad', 'cs.metrics', 'cs.mfa', 'cs.noteslink', 'cs.officelink', 'cs.pcs', 'cs.pdx', 'cs.platform', 'cs.portfolios', 'cs.powerreports', 'cs.projectcosts', 'cs.requirements', 'cs.resources', 'cs.scm', 'cs.taskboard', 'cs.taskmanager', 'cs.threed', 'cs.vp', 'cs.vp-pcs', 'cs.web', 'cs.workflow', 'cs.workspaces', 'cscdb.product'],
    docsets=[
        # Add a relative path for each documentation set in this package
        ],
    cdb_modules=[
        # List the package's modules in the correct (initialization) order as
        # computed by cdb.comparch topological sort. This list goes into
        # `cdb_modules.txt` in the EGG-INFO.
        "rbei.plm"
        ],
    cdb_services=[
        # List the services of this packages by their class names. This list
        # goes into `cdb_services.txt` in EGG-INFO.
        ],
)
