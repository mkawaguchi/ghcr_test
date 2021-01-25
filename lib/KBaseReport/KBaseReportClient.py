# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport
import time


class KBaseReport(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login',
            service_ver='release',
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def _check_job(self, job_id):
        return self._client._check_job('KBaseReport', job_id)

    def _create_submit(self, params, context=None):
        return self._client._submit_job(
             'KBaseReport.create', [params],
             self._service_ver, context)

    def create(self, params, context=None):
        """
        Function signature for the create() method -- generate a simple,
        text-based report for an app run.
        @deprecated KBaseReport.create_extended_report
        :param params: instance of type "CreateParams" (* Parameters for the
           create() method * * Pass in *either* workspace_name or
           workspace_id -- only one is needed. * Note that workspace_id is
           preferred over workspace_name because workspace_id immutable. * *
           Required arguments: *     SimpleReport report - See the structure
           above *     string workspace_name - Workspace name of the running
           app. Required *         if workspace_id is absent *     int
           workspace_id - Workspace ID of the running app. Required if *     
           workspace_name is absent) -> structure: parameter "report" of type
           "SimpleReport" (* A simple report for use in create() * Optional
           arguments: *     string text_message - Readable plain-text report
           message *     string direct_html - Simple HTML text that will be
           rendered within the report widget *     list<string> warnings - A
           list of plain-text warning messages *     list<WorkspaceObject>
           objects_created - List of result workspace objects that this app *
           has created. They will get linked in the report view) ->
           structure: parameter "text_message" of String, parameter
           "direct_html" of String, parameter "warnings" of list of String,
           parameter "objects_created" of list of type "WorkspaceObject" (*
           Represents a Workspace object with some brief description text *
           that can be associated with the object. * Required arguments: *   
           ws_id ref - workspace ID in the format
           'workspace_id/object_id/version' * Optional arguments: *    
           string description - A plaintext, human-readable description of
           the *         object created) -> structure: parameter "ref" of
           type "ws_id" (* Workspace ID reference in the format
           'workspace_id/object_id/version' * @id ws), parameter
           "description" of String, parameter "workspace_name" of String,
           parameter "workspace_id" of Long
        :returns: instance of type "ReportInfo" (* The reference to the saved
           KBaseReport. This is the return object for * both create() and
           create_extended() * Returned data: *    ws_id ref - reference to a
           workspace object in the form of *       
           'workspace_id/object_id/version'. This is a reference to a saved *
           Report object (see KBaseReportWorkspace.spec) *    string name -
           Plaintext unique name for the report. In *        create_extended,
           this can optionally be set in a parameter) -> structure: parameter
           "ref" of type "ws_id" (* Workspace ID reference in the format
           'workspace_id/object_id/version' * @id ws), parameter "name" of
           String
        """
        job_id = self._create_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _create_extended_report_submit(self, params, context=None):
        return self._client._submit_job(
             'KBaseReport.create_extended_report', [params],
             self._service_ver, context)

    def create_extended_report(self, params, context=None):
        """
        Create a report for the results of an app run. This method handles file
        and HTML zipping, uploading, and linking as well as HTML rendering.
        :param params: instance of type "CreateExtendedReportParams" (*
           Parameters used to create a more complex report with file and HTML
           links * * Pass in *either* workspace_name or workspace_id -- only
           one is needed. * Note that workspace_id is preferred over
           workspace_name because workspace_id immutable. * * Required
           arguments: *     string workspace_name - Name of the workspace
           where the report *         should be saved. Required if
           workspace_id is absent *     int workspace_id - ID of workspace
           where the report should be saved. *         Required if
           workspace_name is absent * Optional arguments: *     string
           message - Simple text message to store in the report object *    
           list<WorkspaceObject> objects_created - List of result workspace
           objects that this app *         has created. They will be linked
           in the report view *     list<string> warnings - A list of
           plain-text warning messages *     list<File> html_links - A list
           of paths or shock IDs pointing to HTML files or directories. *    
           If you pass in paths to directories, they will be zipped and
           uploaded *     int direct_html_link_index - Index in html_links to
           set the direct/default view in the *         report. Set either
           direct_html_link_index or direct_html, but not both *     string
           direct_html - Simple HTML text content that will be rendered
           within the report *         widget. Set either direct_html or
           direct_html_link_index, but not both *     list<File> file_links -
           A list of file paths or shock node IDs. Allows the user to *      
           specify files that the report widget should link for download. If
           you pass in paths *         to directories, they will be zipped * 
           string report_object_name - Name to use for the report object
           (will *         be auto-generated if unspecified) *    
           html_window_height - Fixed height in pixels of the HTML window for
           the report *     summary_window_height - Fixed height in pixels of
           the summary window for the report) -> structure: parameter
           "message" of String, parameter "objects_created" of list of type
           "WorkspaceObject" (* Represents a Workspace object with some brief
           description text * that can be associated with the object. *
           Required arguments: *     ws_id ref - workspace ID in the format
           'workspace_id/object_id/version' * Optional arguments: *    
           string description - A plaintext, human-readable description of
           the *         object created) -> structure: parameter "ref" of
           type "ws_id" (* Workspace ID reference in the format
           'workspace_id/object_id/version' * @id ws), parameter
           "description" of String, parameter "warnings" of list of String,
           parameter "html_links" of list of type "File" (* A file to be
           linked in the report. Pass in *either* a shock_id or a * path. If
           a path to a file is given, then the file will be uploaded. If a *
           path to a directory is given, then it will be zipped and uploaded.
           * Required arguments: *     string path - Can be a file or
           directory path. Required if shock_id is absent *     string
           shock_id - Shock node ID. Required if path is absent *     string
           name - Plain-text filename (eg. "results.zip") -- shown to the
           user * Optional arguments: *     string label - A short
           description for the file (eg. "Filter results") *     string
           description - A more detailed, human-readable description of the
           file) -> structure: parameter "path" of String, parameter
           "shock_id" of String, parameter "name" of String, parameter
           "label" of String, parameter "description" of String, parameter
           "direct_html" of String, parameter "direct_html_link_index" of
           Long, parameter "file_links" of list of type "File" (* A file to
           be linked in the report. Pass in *either* a shock_id or a * path.
           If a path to a file is given, then the file will be uploaded. If a
           * path to a directory is given, then it will be zipped and
           uploaded. * Required arguments: *     string path - Can be a file
           or directory path. Required if shock_id is absent *     string
           shock_id - Shock node ID. Required if path is absent *     string
           name - Plain-text filename (eg. "results.zip") -- shown to the
           user * Optional arguments: *     string label - A short
           description for the file (eg. "Filter results") *     string
           description - A more detailed, human-readable description of the
           file) -> structure: parameter "path" of String, parameter
           "shock_id" of String, parameter "name" of String, parameter
           "label" of String, parameter "description" of String, parameter
           "report_object_name" of String, parameter "html_window_height" of
           Double, parameter "summary_window_height" of Double, parameter
           "workspace_name" of String, parameter "workspace_id" of Long
        :returns: instance of type "ReportInfo" (* The reference to the saved
           KBaseReport. This is the return object for * both create() and
           create_extended() * Returned data: *    ws_id ref - reference to a
           workspace object in the form of *       
           'workspace_id/object_id/version'. This is a reference to a saved *
           Report object (see KBaseReportWorkspace.spec) *    string name -
           Plaintext unique name for the report. In *        create_extended,
           this can optionally be set in a parameter) -> structure: parameter
           "ref" of type "ws_id" (* Workspace ID reference in the format
           'workspace_id/object_id/version' * @id ws), parameter "name" of
           String
        """
        job_id = self._create_extended_report_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def status(self, context=None):
        job_id = self._client._submit_job('KBaseReport.status', 
            [], self._service_ver, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]
