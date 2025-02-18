// Package clouddebugger provides access to the Google Cloud Debugger API.
//
// See https://cloud.google.com/tools/cloud-debugger
//
// Usage example:
//
//   import "google.golang.org/api/clouddebugger/v2"
//   ...
//   clouddebuggerService, err := clouddebugger.New(oauthHttpClient)
package clouddebugger

import (
	"bytes"
	"encoding/json"
	"errors"
	"fmt"
	"golang.org/x/net/context"
	"google.golang.org/api/googleapi"
	"io"
	"net/http"
	"net/url"
	"strconv"
	"strings"
)

// Always reference these packages, just in case the auto-generated code
// below doesn't.
var _ = bytes.NewBuffer
var _ = strconv.Itoa
var _ = fmt.Sprintf
var _ = json.NewDecoder
var _ = io.Copy
var _ = url.Parse
var _ = googleapi.Version
var _ = errors.New
var _ = strings.Replace
var _ = context.Background

const apiId = "clouddebugger:v2"
const apiName = "clouddebugger"
const apiVersion = "v2"
const basePath = "https://clouddebugger.googleapis.com/"

// OAuth2 scopes used by this API.
const (
	// View and manage your data across Google Cloud Platform services
	CloudPlatformScope = "https://www.googleapis.com/auth/cloud-platform"

	// Manage cloud debugger
	CloudDebuggerScope = "https://www.googleapis.com/auth/cloud_debugger"

	// Manage active breakpoints in cloud debugger
	CloudDebugletcontrollerScope = "https://www.googleapis.com/auth/cloud_debugletcontroller"
)

func New(client *http.Client) (*Service, error) {
	if client == nil {
		return nil, errors.New("client is nil")
	}
	s := &Service{client: client, BasePath: basePath}
	s.Controller = NewControllerService(s)
	s.Debugger = NewDebuggerService(s)
	return s, nil
}

type Service struct {
	client    *http.Client
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	Controller *ControllerService

	Debugger *DebuggerService
}

func (s *Service) userAgent() string {
	if s.UserAgent == "" {
		return googleapi.UserAgent
	}
	return googleapi.UserAgent + " " + s.UserAgent
}

func NewControllerService(s *Service) *ControllerService {
	rs := &ControllerService{s: s}
	rs.Debuggees = NewControllerDebuggeesService(s)
	return rs
}

type ControllerService struct {
	s *Service

	Debuggees *ControllerDebuggeesService
}

func NewControllerDebuggeesService(s *Service) *ControllerDebuggeesService {
	rs := &ControllerDebuggeesService{s: s}
	rs.Breakpoints = NewControllerDebuggeesBreakpointsService(s)
	return rs
}

type ControllerDebuggeesService struct {
	s *Service

	Breakpoints *ControllerDebuggeesBreakpointsService
}

func NewControllerDebuggeesBreakpointsService(s *Service) *ControllerDebuggeesBreakpointsService {
	rs := &ControllerDebuggeesBreakpointsService{s: s}
	return rs
}

type ControllerDebuggeesBreakpointsService struct {
	s *Service
}

func NewDebuggerService(s *Service) *DebuggerService {
	rs := &DebuggerService{s: s}
	rs.Debuggees = NewDebuggerDebuggeesService(s)
	return rs
}

type DebuggerService struct {
	s *Service

	Debuggees *DebuggerDebuggeesService
}

func NewDebuggerDebuggeesService(s *Service) *DebuggerDebuggeesService {
	rs := &DebuggerDebuggeesService{s: s}
	rs.Breakpoints = NewDebuggerDebuggeesBreakpointsService(s)
	return rs
}

type DebuggerDebuggeesService struct {
	s *Service

	Breakpoints *DebuggerDebuggeesBreakpointsService
}

func NewDebuggerDebuggeesBreakpointsService(s *Service) *DebuggerDebuggeesBreakpointsService {
	rs := &DebuggerDebuggeesBreakpointsService{s: s}
	return rs
}

type DebuggerDebuggeesBreakpointsService struct {
	s *Service
}

type Breakpoint struct {
	// Action: Defines what to do when the breakpoint hits.
	//
	// Possible values:
	//   "CAPTURE"
	//   "LOG"
	Action string `json:"action,omitempty"`

	// Condition: A condition to trigger the breakpoint. The condition is a
	// compound boolean expression composed using expressions in a
	// programming language at the source location.
	Condition string `json:"condition,omitempty"`

	// CreateTime: The time this breakpoint was created by the server. The
	// value is in seconds resolution.
	CreateTime string `json:"createTime,omitempty"`

	// EvaluatedExpressions: The evaluated expressions' values at breakpoint
	// time. The evaluated expressions appear in exactly the same order they
	// are listed in the 'expressions' field. The 'name' field holds the
	// original expression text, the 'value'/'members' field holds the
	// result of the evaluated expression. If the expression can not be
	// evaluated, an error text is placed in the value field.
	EvaluatedExpressions []*Variable `json:"evaluatedExpressions,omitempty"`

	// Expressions: A list of read-only expressions to evaluate at the
	// breakpoint location. The expressions are composed using expressions
	// in the programming language at the source location. If the breakpoint
	// action is "LOG", the evaluated expressions are included in log
	// statements.
	Expressions []string `json:"expressions,omitempty"`

	// FinalTime: The time this breakpoint was finalized as seen by the
	// server. The value is in seconds resolution.
	FinalTime string `json:"finalTime,omitempty"`

	// Id: Breakpoint identifier, unique in the scope of the debuggee.
	Id string `json:"id,omitempty"`

	// IsFinalState: When true, indicates that this is a final result and
	// the breakpoint state will not change from here on.
	IsFinalState bool `json:"isFinalState,omitempty"`

	// Location: The breakpoint source location.
	Location *SourceLocation `json:"location,omitempty"`

	// LogLevel: Indicates the severity of the log. Only relevant when
	// action is "LOG".
	//
	// Possible values:
	//   "INFO"
	//   "WARNING"
	//   "ERROR"
	LogLevel string `json:"logLevel,omitempty"`

	// LogMessageFormat: Only relevant when action is "LOG". Defines the
	// message to log when the breakpoint hits. The message may include
	// parameter placeholders "$0", "$1", etc. These placeholders will be
	// replaced with the evaluated value of the appropriate expression.
	// Expressions not referenced in "log_message_format" will not be
	// logged. Example: "Poisonous message received, id = $0, count = $1"
	// with expressions = [ "message.id", "message.count" ].
	LogMessageFormat string `json:"logMessageFormat,omitempty"`

	// StackFrames: The stack at breakpoint time.
	StackFrames []*StackFrame `json:"stackFrames,omitempty"`

	// Status: Breakpoint status. The status includes an error flag and a
	// human readable message. This field will usually stay unset. The
	// message can be either informational or error. Nevertheless, clients
	// should always display the text message back to the user. Error status
	// of a breakpoint indicates complete failure. Example (non-final
	// state): 'Still loading symbols...' Examples (final state): 'Failed to
	// insert breakpoint' referring to breakpoint, 'Field f not found in
	// class C' referring to condition, ...
	Status *StatusMessage `json:"status,omitempty"`

	// UserEmail: The e-mail of the user that created this breakpoint
	UserEmail string `json:"userEmail,omitempty"`

	// VariableTable: The variable_table exists to aid with computation,
	// memory and network traffic optimization. It enables storing a
	// variable once and reference it from multiple variables, including
	// variables stored in the variable_table itself. For example, the
	// object 'this', which may appear at many levels of the stack, can have
	// all of it's data stored once in this table. The stack frame variables
	// then would hold only a reference to it. The variable var_index field
	// is an index into this repeated field. The stored objects are nameless
	// and get their name from the referencing variable. The effective
	// variable is a merge of the referencing veariable and the referenced
	// variable.
	VariableTable []*Variable `json:"variableTable,omitempty"`
}

type CloudRepoSourceContext struct {
	// AliasName: The name of an alias (branch, tag, etc.).
	AliasName string `json:"aliasName,omitempty"`

	// RepoId: The ID of the repo.
	RepoId *RepoId `json:"repoId,omitempty"`

	// RevisionId: A revision ID.
	RevisionId string `json:"revisionId,omitempty"`
}

type CloudWorkspaceId struct {
	// Name: The unique name of the workspace within the repo. This is the
	// name chosen by the client in the Source API's CreateWorkspace method.
	Name string `json:"name,omitempty"`

	// RepoId: The ID of the repo containing the workspace.
	RepoId *RepoId `json:"repoId,omitempty"`
}

type CloudWorkspaceSourceContext struct {
	// SnapshotId: The ID of the snapshot. An empty snapshot_id refers to
	// the most recent snapshot.
	SnapshotId string `json:"snapshotId,omitempty"`

	// WorkspaceId: The ID of the workspace.
	WorkspaceId *CloudWorkspaceId `json:"workspaceId,omitempty"`
}

type Debuggee struct {
	// AgentVersion: Version ID of the agent release. The version ID is
	// structured as following: "domain/type/vmajor.minor" (for example
	// "google.com/gcp-java/v1.1").
	AgentVersion string `json:"agentVersion,omitempty"`

	// Description: A human readable description of the debuggee.
	// Recommended to include human readable project name, environment name,
	// and version information .
	Description string `json:"description,omitempty"`

	// Id: Debuggee unique identifer generated by the server.
	Id string `json:"id,omitempty"`

	// IsDisabled: If set to true, indicates that the agent should disable
	// itself and detach from the debuggee.
	IsDisabled bool `json:"isDisabled,omitempty"`

	// IsInactive: If set to true indicates that the debuggee has not been
	// seen by the Controller service in the last active time period
	// (defined by the server).
	IsInactive bool `json:"isInactive,omitempty"`

	// Labels: A set of custom debuggee properties, populated by the agent,
	// to be displayed to the user.
	Labels map[string]string `json:"labels,omitempty"`

	// Project: The project the debuggee is associated with. Use the project
	// number when registering a Google Cloud Platform project.
	Project string `json:"project,omitempty"`

	// SourceContexts: Repository snapshots containing the source code of
	// the project.
	SourceContexts []*SourceContext `json:"sourceContexts,omitempty"`

	// Status: Human readable message to be displayed to the user about this
	// debuggee. Absense of this field indicates no message. The message can
	// be either informational or error.
	Status *StatusMessage `json:"status,omitempty"`

	// Uniquifier: The debuggee uniqifier within the project. Any string
	// that id the application within the project can be used. Recomended to
	// include environement and version or build id's.
	Uniquifier string `json:"uniquifier,omitempty"`
}

type Empty struct {
}

type FormatMessage struct {
	// Format: Format template of the message. The "format" uses
	// placeholders "$0", "$1", etc. to reference parameters. "$$" can be
	// used to denote the '$' character. Examples: "Failed to load '$0'
	// which helps debug $1 the first time it is loaded. Again, $0 is very
	// important." "Please pay $$10 to use $0 instead of $1."
	Format string `json:"format,omitempty"`

	// Parameters: Optional parameters to be embedded into the message.
	Parameters []string `json:"parameters,omitempty"`
}

type GerritSourceContext struct {
	// AliasName: The name of an alias (branch, tag, etc.).
	AliasName string `json:"aliasName,omitempty"`

	// GerritProject: The full project name within the host. Projects may be
	// nested, so "project/subproject" is a valid project name. The "repo
	// name" is hostURI/project.
	GerritProject string `json:"gerritProject,omitempty"`

	// HostUri: The URI of a running Gerrit instance.
	HostUri string `json:"hostUri,omitempty"`

	// RevisionId: A revision (commit) ID.
	RevisionId string `json:"revisionId,omitempty"`
}

type GetBreakpointResponse struct {
	// Breakpoint: The complete breakpoint state. The fields 'id' and
	// 'location' are guranteed to be set.
	Breakpoint *Breakpoint `json:"breakpoint,omitempty"`
}

type ListActiveBreakpointsResponse struct {
	// Breakpoints: List of all active breakpoints. The fields 'id' and
	// 'location' are guranteed to be set on each breakpoint.
	Breakpoints []*Breakpoint `json:"breakpoints,omitempty"`

	// NextWaitToken: A wait token that can be used in the next method call
	// to block until the list of breakpoints changes.
	NextWaitToken string `json:"nextWaitToken,omitempty"`
}

type ListBreakpointsResponse struct {
	// Breakpoints: List of all breakpoints with complete state. The fields
	// 'id' and 'location' are guranteed to be set on each breakpoint.
	Breakpoints []*Breakpoint `json:"breakpoints,omitempty"`

	// NextWaitToken: A wait token that can be used in the next call to
	// ListBreakpoints to block until the list of breakpoints has changes.
	NextWaitToken string `json:"nextWaitToken,omitempty"`
}

type ListDebuggeesResponse struct {
	// Debuggees: The list of debuggees accessible to the calling user. Note
	// that the description field is the only human readable field that
	// should be displayed to the user. The fields 'debuggee.id' and
	// 'description' are guranteed to be set on each debuggee.
	Debuggees []*Debuggee `json:"debuggees,omitempty"`
}

type ProjectRepoId struct {
	// ProjectId: The ID of the project.
	ProjectId string `json:"projectId,omitempty"`

	// RepoName: The name of the repo. Leave empty for the default repo.
	RepoName string `json:"repoName,omitempty"`
}

type RegisterDebuggeeRequest struct {
	// Debuggee: The debuggee information to register. The fields 'project',
	// 'uniquifier', 'description' and 'agent_version' of the debuggee must
	// be set.
	Debuggee *Debuggee `json:"debuggee,omitempty"`
}

type RegisterDebuggeeResponse struct {
	// Debuggee: The debuggee resource. The field 'id' is guranteed to be
	// set (in addition to the echoed fields).
	Debuggee *Debuggee `json:"debuggee,omitempty"`
}

type RepoId struct {
	// ProjectRepoId: A combination of a project ID and a repo name.
	ProjectRepoId *ProjectRepoId `json:"projectRepoId,omitempty"`

	// Uid: A server-assigned, globally unique identifier.
	Uid string `json:"uid,omitempty"`
}

type SetBreakpointResponse struct {
	// Breakpoint: The breakpoint resource. The field 'id' is guranteed to
	// be set (in addition to the echoed fileds).
	Breakpoint *Breakpoint `json:"breakpoint,omitempty"`
}

type SourceContext struct {
	// CloudRepo: A SourceContext referring to a revision in a cloud repo.
	CloudRepo *CloudRepoSourceContext `json:"cloudRepo,omitempty"`

	// CloudWorkspace: A SourceContext referring to a snapshot in a cloud
	// workspace.
	CloudWorkspace *CloudWorkspaceSourceContext `json:"cloudWorkspace,omitempty"`

	// Gerrit: A SourceContext referring to a Gerrit project.
	Gerrit *GerritSourceContext `json:"gerrit,omitempty"`
}

type SourceLocation struct {
	// Line: The line inside the file (first line value is '1').
	Line int64 `json:"line,omitempty"`

	// Path: A path to the source file within the source context of the
	// target binary.
	Path string `json:"path,omitempty"`
}

type StackFrame struct {
	// Arguments: The set of arguments passed to this function Note that
	// this might not be populated for all stack frames.
	Arguments []*Variable `json:"arguments,omitempty"`

	// Function: The unmangled function name at the call site.
	Function string `json:"function,omitempty"`

	// Locals: The set of local variables at the stack frame location. Note
	// that this might not be populated for all stack frames.
	Locals []*Variable `json:"locals,omitempty"`

	// Location: The source location of the call site.
	Location *SourceLocation `json:"location,omitempty"`
}

type StatusMessage struct {
	// Description: Status message text.
	Description *FormatMessage `json:"description,omitempty"`

	// IsError: Distinguishes errors from informational messages.
	IsError bool `json:"isError,omitempty"`

	// RefersTo: Reference to which the message applies.
	//
	// Possible values:
	//   "UNSPECIFIED"
	//   "BREAKPOINT_SOURCE_LOCATION"
	//   "BREAKPOINT_CONDITION"
	//   "BREAKPOINT_EXPRESSION"
	//   "VARIABLE_NAME"
	//   "VARIABLE_VALUE"
	RefersTo string `json:"refersTo,omitempty"`
}

type UpdateActiveBreakpointRequest struct {
	// Breakpoint: The updated breakpoint information. The field 'id' must
	// be set.
	Breakpoint *Breakpoint `json:"breakpoint,omitempty"`
}

type UpdateActiveBreakpointResponse struct {
}

type Variable struct {
	// Members: The members contained or pointed to by the variable.
	Members []*Variable `json:"members,omitempty"`

	// Name: The name of the variable, if any.
	Name string `json:"name,omitempty"`

	// Status: Status associated with the variable. This field will usually
	// stay unset. A status of a single variable only applies to that
	// variable or expression. The rest of breakpoint data still remains
	// valid. Variables might be reported in error state even when
	// breakpoint is not in final state. The message may refer to variable
	// name with "refers_to" set to "VARIABLE_NAME". Alternatively
	// "refers_to" will be set to "VARIABLE_VALUE". In either case variable
	// value and members will be unset. Example of error message applied to
	// name: "Invalid expression syntax". Example of information message
	// applied to value: "Not captured". Examples of error message applied
	// to value: "Malformed string", "Field f not found in class C", "Null
	// pointer dereference".
	Status *StatusMessage `json:"status,omitempty"`

	// Value: The simple value of the variable.
	Value string `json:"value,omitempty"`

	// VarTableIndex: This is a reference to a variable in the shared
	// variable table. More than one variable can reference the same
	// variable in the table. The var_index field is an index into
	// variable_table in Breakpoint.
	VarTableIndex int64 `json:"varTableIndex,omitempty"`
}

// method id "clouddebugger.controller.debuggees.register":

type ControllerDebuggeesRegisterCall struct {
	s                       *Service
	registerdebuggeerequest *RegisterDebuggeeRequest
	opt_                    map[string]interface{}
}

// Register: Registers the debuggee with the controller. All agents
// should call this API with the same request content to get back the
// same stable 'debuggee_id'. Agents should call this API again whenever
// ListActiveBreakpoints or UpdateActiveBreakpoint return the error
// google.rpc.Code.NOT_FOUND. It allows the server to disable the agent
// or recover from any registration loss. If the debuggee is disabled
// server, the response will have is_disabled' set to true.
func (r *ControllerDebuggeesService) Register(registerdebuggeerequest *RegisterDebuggeeRequest) *ControllerDebuggeesRegisterCall {
	c := &ControllerDebuggeesRegisterCall{s: r.s, opt_: make(map[string]interface{})}
	c.registerdebuggeerequest = registerdebuggeerequest
	return c
}

// Fields allows partial responses to be retrieved.
// See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse
// for more information.
func (c *ControllerDebuggeesRegisterCall) Fields(s ...googleapi.Field) *ControllerDebuggeesRegisterCall {
	c.opt_["fields"] = googleapi.CombineFields(s)
	return c
}

func (c *ControllerDebuggeesRegisterCall) Do() (*RegisterDebuggeeResponse, error) {
	var body io.Reader = nil
	body, err := googleapi.WithoutDataWrapper.JSONReader(c.registerdebuggeerequest)
	if err != nil {
		return nil, err
	}
	ctype := "application/json"
	params := make(url.Values)
	params.Set("alt", "json")
	if v, ok := c.opt_["fields"]; ok {
		params.Set("fields", fmt.Sprintf("%v", v))
	}
	urls := googleapi.ResolveRelative(c.s.BasePath, "v2/controller/debuggees/register")
	urls += "?" + params.Encode()
	req, _ := http.NewRequest("POST", urls, body)
	googleapi.SetOpaque(req.URL)
	req.Header.Set("Content-Type", ctype)
	req.Header.Set("User-Agent", c.s.userAgent())
	res, err := c.s.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer googleapi.CloseBody(res)
	if err := googleapi.CheckResponse(res); err != nil {
		return nil, err
	}
	var ret *RegisterDebuggeeResponse
	if err := json.NewDecoder(res.Body).Decode(&ret); err != nil {
		return nil, err
	}
	return ret, nil
	// {
	//   "description": "Registers the debuggee with the controller. All agents should call this API with the same request content to get back the same stable 'debuggee_id'. Agents should call this API again whenever ListActiveBreakpoints or UpdateActiveBreakpoint return the error google.rpc.Code.NOT_FOUND. It allows the server to disable the agent or recover from any registration loss. If the debuggee is disabled server, the response will have is_disabled' set to true.",
	//   "httpMethod": "POST",
	//   "id": "clouddebugger.controller.debuggees.register",
	//   "path": "v2/controller/debuggees/register",
	//   "request": {
	//     "$ref": "RegisterDebuggeeRequest"
	//   },
	//   "response": {
	//     "$ref": "RegisterDebuggeeResponse"
	//   },
	//   "scopes": [
	//     "https://www.googleapis.com/auth/cloud-platform",
	//     "https://www.googleapis.com/auth/cloud_debugletcontroller"
	//   ]
	// }

}

// method id "clouddebugger.controller.debuggees.breakpoints.list":

type ControllerDebuggeesBreakpointsListCall struct {
	s          *Service
	debuggeeId string
	opt_       map[string]interface{}
}

// List: Returns the list of all active breakpoints for the specified
// debuggee. The breakpoint specification (location, condition, and
// expression fields) is semantically immutable, although the field
// values may change. For example, an agent may update the location line
// number to reflect the actual line the breakpoint was set to, but that
// doesn't change the breakpoint semantics. Thus, an agent does not need
// to check if a breakpoint has changed when it encounters the same
// breakpoint on a successive call. Moreover, an agent should remember
// breakpoints that are complete until the controller removes them from
// the active list to avoid setting those breakpoints again.
func (r *ControllerDebuggeesBreakpointsService) List(debuggeeId string) *ControllerDebuggeesBreakpointsListCall {
	c := &ControllerDebuggeesBreakpointsListCall{s: r.s, opt_: make(map[string]interface{})}
	c.debuggeeId = debuggeeId
	return c
}

// WaitToken sets the optional parameter "waitToken": A wait token that,
// if specified, blocks the method call until the list of active
// breakpoints has changed, or a server selected timeout has expired.
// The value should be set from the last returned response. The error
// code google.rpc.Code.ABORTED is returned on wait timeout (which does
// not require the agent to re-register with the server)
func (c *ControllerDebuggeesBreakpointsListCall) WaitToken(waitToken string) *ControllerDebuggeesBreakpointsListCall {
	c.opt_["waitToken"] = waitToken
	return c
}

// Fields allows partial responses to be retrieved.
// See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse
// for more information.
func (c *ControllerDebuggeesBreakpointsListCall) Fields(s ...googleapi.Field) *ControllerDebuggeesBreakpointsListCall {
	c.opt_["fields"] = googleapi.CombineFields(s)
	return c
}

func (c *ControllerDebuggeesBreakpointsListCall) Do() (*ListActiveBreakpointsResponse, error) {
	var body io.Reader = nil
	params := make(url.Values)
	params.Set("alt", "json")
	if v, ok := c.opt_["waitToken"]; ok {
		params.Set("waitToken", fmt.Sprintf("%v", v))
	}
	if v, ok := c.opt_["fields"]; ok {
		params.Set("fields", fmt.Sprintf("%v", v))
	}
	urls := googleapi.ResolveRelative(c.s.BasePath, "v2/controller/debuggees/{debuggeeId}/breakpoints")
	urls += "?" + params.Encode()
	req, _ := http.NewRequest("GET", urls, body)
	googleapi.Expand(req.URL, map[string]string{
		"debuggeeId": c.debuggeeId,
	})
	req.Header.Set("User-Agent", c.s.userAgent())
	res, err := c.s.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer googleapi.CloseBody(res)
	if err := googleapi.CheckResponse(res); err != nil {
		return nil, err
	}
	var ret *ListActiveBreakpointsResponse
	if err := json.NewDecoder(res.Body).Decode(&ret); err != nil {
		return nil, err
	}
	return ret, nil
	// {
	//   "description": "Returns the list of all active breakpoints for the specified debuggee. The breakpoint specification (location, condition, and expression fields) is semantically immutable, although the field values may change. For example, an agent may update the location line number to reflect the actual line the breakpoint was set to, but that doesn't change the breakpoint semantics. Thus, an agent does not need to check if a breakpoint has changed when it encounters the same breakpoint on a successive call. Moreover, an agent should remember breakpoints that are complete until the controller removes them from the active list to avoid setting those breakpoints again.",
	//   "httpMethod": "GET",
	//   "id": "clouddebugger.controller.debuggees.breakpoints.list",
	//   "parameterOrder": [
	//     "debuggeeId"
	//   ],
	//   "parameters": {
	//     "debuggeeId": {
	//       "description": "Identifies the debuggee.",
	//       "location": "path",
	//       "required": true,
	//       "type": "string"
	//     },
	//     "waitToken": {
	//       "description": "A wait token that, if specified, blocks the method call until the list of active breakpoints has changed, or a server selected timeout has expired. The value should be set from the last returned response. The error code google.rpc.Code.ABORTED is returned on wait timeout (which does not require the agent to re-register with the server)",
	//       "location": "query",
	//       "type": "string"
	//     }
	//   },
	//   "path": "v2/controller/debuggees/{debuggeeId}/breakpoints",
	//   "response": {
	//     "$ref": "ListActiveBreakpointsResponse"
	//   },
	//   "scopes": [
	//     "https://www.googleapis.com/auth/cloud-platform",
	//     "https://www.googleapis.com/auth/cloud_debugletcontroller"
	//   ]
	// }

}

// method id "clouddebugger.controller.debuggees.breakpoints.update":

type ControllerDebuggeesBreakpointsUpdateCall struct {
	s                             *Service
	debuggeeId                    string
	id                            string
	updateactivebreakpointrequest *UpdateActiveBreakpointRequest
	opt_                          map[string]interface{}
}

// Update: Updates the breakpoint state or mutable fields. The entire
// Breakpoint protobuf must be sent back to the controller. Updates to
// active breakpoint fields are only allowed if the new value does not
// change the breakpoint specification. Updates to the 'location',
// 'condition' and 'expression' fields should not alter the breakpoint
// semantics. They are restricted to changes such as canonicalizing a
// value or snapping the location to the correct line of code.
func (r *ControllerDebuggeesBreakpointsService) Update(debuggeeId string, id string, updateactivebreakpointrequest *UpdateActiveBreakpointRequest) *ControllerDebuggeesBreakpointsUpdateCall {
	c := &ControllerDebuggeesBreakpointsUpdateCall{s: r.s, opt_: make(map[string]interface{})}
	c.debuggeeId = debuggeeId
	c.id = id
	c.updateactivebreakpointrequest = updateactivebreakpointrequest
	return c
}

// Fields allows partial responses to be retrieved.
// See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse
// for more information.
func (c *ControllerDebuggeesBreakpointsUpdateCall) Fields(s ...googleapi.Field) *ControllerDebuggeesBreakpointsUpdateCall {
	c.opt_["fields"] = googleapi.CombineFields(s)
	return c
}

func (c *ControllerDebuggeesBreakpointsUpdateCall) Do() (*UpdateActiveBreakpointResponse, error) {
	var body io.Reader = nil
	body, err := googleapi.WithoutDataWrapper.JSONReader(c.updateactivebreakpointrequest)
	if err != nil {
		return nil, err
	}
	ctype := "application/json"
	params := make(url.Values)
	params.Set("alt", "json")
	if v, ok := c.opt_["fields"]; ok {
		params.Set("fields", fmt.Sprintf("%v", v))
	}
	urls := googleapi.ResolveRelative(c.s.BasePath, "v2/controller/debuggees/{debuggeeId}/breakpoints/{id}")
	urls += "?" + params.Encode()
	req, _ := http.NewRequest("PUT", urls, body)
	googleapi.Expand(req.URL, map[string]string{
		"debuggeeId": c.debuggeeId,
		"id":         c.id,
	})
	req.Header.Set("Content-Type", ctype)
	req.Header.Set("User-Agent", c.s.userAgent())
	res, err := c.s.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer googleapi.CloseBody(res)
	if err := googleapi.CheckResponse(res); err != nil {
		return nil, err
	}
	var ret *UpdateActiveBreakpointResponse
	if err := json.NewDecoder(res.Body).Decode(&ret); err != nil {
		return nil, err
	}
	return ret, nil
	// {
	//   "description": "Updates the breakpoint state or mutable fields. The entire Breakpoint protobuf must be sent back to the controller. Updates to active breakpoint fields are only allowed if the new value does not change the breakpoint specification. Updates to the 'location', 'condition' and 'expression' fields should not alter the breakpoint semantics. They are restricted to changes such as canonicalizing a value or snapping the location to the correct line of code.",
	//   "httpMethod": "PUT",
	//   "id": "clouddebugger.controller.debuggees.breakpoints.update",
	//   "parameterOrder": [
	//     "debuggeeId",
	//     "id"
	//   ],
	//   "parameters": {
	//     "debuggeeId": {
	//       "description": "Identifies the debuggee being debugged.",
	//       "location": "path",
	//       "required": true,
	//       "type": "string"
	//     },
	//     "id": {
	//       "description": "Breakpoint identifier, unique in the scope of the debuggee.",
	//       "location": "path",
	//       "required": true,
	//       "type": "string"
	//     }
	//   },
	//   "path": "v2/controller/debuggees/{debuggeeId}/breakpoints/{id}",
	//   "request": {
	//     "$ref": "UpdateActiveBreakpointRequest"
	//   },
	//   "response": {
	//     "$ref": "UpdateActiveBreakpointResponse"
	//   },
	//   "scopes": [
	//     "https://www.googleapis.com/auth/cloud-platform",
	//     "https://www.googleapis.com/auth/cloud_debugletcontroller"
	//   ]
	// }

}

// method id "clouddebugger.debugger.debuggees.list":

type DebuggerDebuggeesListCall struct {
	s    *Service
	opt_ map[string]interface{}
}

// List: Lists all the debuggees that the user can set breakpoints to.
func (r *DebuggerDebuggeesService) List() *DebuggerDebuggeesListCall {
	c := &DebuggerDebuggeesListCall{s: r.s, opt_: make(map[string]interface{})}
	return c
}

// IncludeInactive sets the optional parameter "includeInactive": When
// set to true the result includes all debuggees, otherwise only
// debugees that are active.
func (c *DebuggerDebuggeesListCall) IncludeInactive(includeInactive bool) *DebuggerDebuggeesListCall {
	c.opt_["includeInactive"] = includeInactive
	return c
}

// Project sets the optional parameter "project": Set to the project
// number of the Google Cloud Platform to list the debuggees that are
// part of that project.
func (c *DebuggerDebuggeesListCall) Project(project string) *DebuggerDebuggeesListCall {
	c.opt_["project"] = project
	return c
}

// Fields allows partial responses to be retrieved.
// See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse
// for more information.
func (c *DebuggerDebuggeesListCall) Fields(s ...googleapi.Field) *DebuggerDebuggeesListCall {
	c.opt_["fields"] = googleapi.CombineFields(s)
	return c
}

func (c *DebuggerDebuggeesListCall) Do() (*ListDebuggeesResponse, error) {
	var body io.Reader = nil
	params := make(url.Values)
	params.Set("alt", "json")
	if v, ok := c.opt_["includeInactive"]; ok {
		params.Set("includeInactive", fmt.Sprintf("%v", v))
	}
	if v, ok := c.opt_["project"]; ok {
		params.Set("project", fmt.Sprintf("%v", v))
	}
	if v, ok := c.opt_["fields"]; ok {
		params.Set("fields", fmt.Sprintf("%v", v))
	}
	urls := googleapi.ResolveRelative(c.s.BasePath, "v2/debugger/debuggees")
	urls += "?" + params.Encode()
	req, _ := http.NewRequest("GET", urls, body)
	googleapi.SetOpaque(req.URL)
	req.Header.Set("User-Agent", c.s.userAgent())
	res, err := c.s.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer googleapi.CloseBody(res)
	if err := googleapi.CheckResponse(res); err != nil {
		return nil, err
	}
	var ret *ListDebuggeesResponse
	if err := json.NewDecoder(res.Body).Decode(&ret); err != nil {
		return nil, err
	}
	return ret, nil
	// {
	//   "description": "Lists all the debuggees that the user can set breakpoints to.",
	//   "httpMethod": "GET",
	//   "id": "clouddebugger.debugger.debuggees.list",
	//   "parameters": {
	//     "includeInactive": {
	//       "description": "When set to true the result includes all debuggees, otherwise only debugees that are active.",
	//       "location": "query",
	//       "type": "boolean"
	//     },
	//     "project": {
	//       "description": "Set to the project number of the Google Cloud Platform to list the debuggees that are part of that project.",
	//       "location": "query",
	//       "type": "string"
	//     }
	//   },
	//   "path": "v2/debugger/debuggees",
	//   "response": {
	//     "$ref": "ListDebuggeesResponse"
	//   },
	//   "scopes": [
	//     "https://www.googleapis.com/auth/cloud-platform",
	//     "https://www.googleapis.com/auth/cloud_debugger"
	//   ]
	// }

}

// method id "clouddebugger.debugger.debuggees.breakpoints.delete":

type DebuggerDebuggeesBreakpointsDeleteCall struct {
	s            *Service
	debuggeeId   string
	breakpointId string
	opt_         map[string]interface{}
}

// Delete: Deletes the breakpoint from the debuggee.
func (r *DebuggerDebuggeesBreakpointsService) Delete(debuggeeId string, breakpointId string) *DebuggerDebuggeesBreakpointsDeleteCall {
	c := &DebuggerDebuggeesBreakpointsDeleteCall{s: r.s, opt_: make(map[string]interface{})}
	c.debuggeeId = debuggeeId
	c.breakpointId = breakpointId
	return c
}

// Fields allows partial responses to be retrieved.
// See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse
// for more information.
func (c *DebuggerDebuggeesBreakpointsDeleteCall) Fields(s ...googleapi.Field) *DebuggerDebuggeesBreakpointsDeleteCall {
	c.opt_["fields"] = googleapi.CombineFields(s)
	return c
}

func (c *DebuggerDebuggeesBreakpointsDeleteCall) Do() (*Empty, error) {
	var body io.Reader = nil
	params := make(url.Values)
	params.Set("alt", "json")
	if v, ok := c.opt_["fields"]; ok {
		params.Set("fields", fmt.Sprintf("%v", v))
	}
	urls := googleapi.ResolveRelative(c.s.BasePath, "v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}")
	urls += "?" + params.Encode()
	req, _ := http.NewRequest("DELETE", urls, body)
	googleapi.Expand(req.URL, map[string]string{
		"debuggeeId":   c.debuggeeId,
		"breakpointId": c.breakpointId,
	})
	req.Header.Set("User-Agent", c.s.userAgent())
	res, err := c.s.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer googleapi.CloseBody(res)
	if err := googleapi.CheckResponse(res); err != nil {
		return nil, err
	}
	var ret *Empty
	if err := json.NewDecoder(res.Body).Decode(&ret); err != nil {
		return nil, err
	}
	return ret, nil
	// {
	//   "description": "Deletes the breakpoint from the debuggee.",
	//   "httpMethod": "DELETE",
	//   "id": "clouddebugger.debugger.debuggees.breakpoints.delete",
	//   "parameterOrder": [
	//     "debuggeeId",
	//     "breakpointId"
	//   ],
	//   "parameters": {
	//     "breakpointId": {
	//       "description": "The breakpoint to delete.",
	//       "location": "path",
	//       "required": true,
	//       "type": "string"
	//     },
	//     "debuggeeId": {
	//       "description": "The debuggee id to delete the breakpoint from.",
	//       "location": "path",
	//       "required": true,
	//       "type": "string"
	//     }
	//   },
	//   "path": "v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}",
	//   "response": {
	//     "$ref": "Empty"
	//   },
	//   "scopes": [
	//     "https://www.googleapis.com/auth/cloud-platform",
	//     "https://www.googleapis.com/auth/cloud_debugger"
	//   ]
	// }

}

// method id "clouddebugger.debugger.debuggees.breakpoints.get":

type DebuggerDebuggeesBreakpointsGetCall struct {
	s            *Service
	debuggeeId   string
	breakpointId string
	opt_         map[string]interface{}
}

// Get: Gets breakpoint information.
func (r *DebuggerDebuggeesBreakpointsService) Get(debuggeeId string, breakpointId string) *DebuggerDebuggeesBreakpointsGetCall {
	c := &DebuggerDebuggeesBreakpointsGetCall{s: r.s, opt_: make(map[string]interface{})}
	c.debuggeeId = debuggeeId
	c.breakpointId = breakpointId
	return c
}

// Fields allows partial responses to be retrieved.
// See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse
// for more information.
func (c *DebuggerDebuggeesBreakpointsGetCall) Fields(s ...googleapi.Field) *DebuggerDebuggeesBreakpointsGetCall {
	c.opt_["fields"] = googleapi.CombineFields(s)
	return c
}

func (c *DebuggerDebuggeesBreakpointsGetCall) Do() (*GetBreakpointResponse, error) {
	var body io.Reader = nil
	params := make(url.Values)
	params.Set("alt", "json")
	if v, ok := c.opt_["fields"]; ok {
		params.Set("fields", fmt.Sprintf("%v", v))
	}
	urls := googleapi.ResolveRelative(c.s.BasePath, "v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}")
	urls += "?" + params.Encode()
	req, _ := http.NewRequest("GET", urls, body)
	googleapi.Expand(req.URL, map[string]string{
		"debuggeeId":   c.debuggeeId,
		"breakpointId": c.breakpointId,
	})
	req.Header.Set("User-Agent", c.s.userAgent())
	res, err := c.s.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer googleapi.CloseBody(res)
	if err := googleapi.CheckResponse(res); err != nil {
		return nil, err
	}
	var ret *GetBreakpointResponse
	if err := json.NewDecoder(res.Body).Decode(&ret); err != nil {
		return nil, err
	}
	return ret, nil
	// {
	//   "description": "Gets breakpoint information.",
	//   "httpMethod": "GET",
	//   "id": "clouddebugger.debugger.debuggees.breakpoints.get",
	//   "parameterOrder": [
	//     "debuggeeId",
	//     "breakpointId"
	//   ],
	//   "parameters": {
	//     "breakpointId": {
	//       "description": "The breakpoint to get.",
	//       "location": "path",
	//       "required": true,
	//       "type": "string"
	//     },
	//     "debuggeeId": {
	//       "description": "The debuggee id to get the breakpoint from.",
	//       "location": "path",
	//       "required": true,
	//       "type": "string"
	//     }
	//   },
	//   "path": "v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}",
	//   "response": {
	//     "$ref": "GetBreakpointResponse"
	//   },
	//   "scopes": [
	//     "https://www.googleapis.com/auth/cloud-platform",
	//     "https://www.googleapis.com/auth/cloud_debugger"
	//   ]
	// }

}

// method id "clouddebugger.debugger.debuggees.breakpoints.list":

type DebuggerDebuggeesBreakpointsListCall struct {
	s          *Service
	debuggeeId string
	opt_       map[string]interface{}
}

// List: Lists all breakpoints of the debuggee that the user has access
// to.
func (r *DebuggerDebuggeesBreakpointsService) List(debuggeeId string) *DebuggerDebuggeesBreakpointsListCall {
	c := &DebuggerDebuggeesBreakpointsListCall{s: r.s, opt_: make(map[string]interface{})}
	c.debuggeeId = debuggeeId
	return c
}

// ActionValue sets the optional parameter "action.value": Only
// breakpoints with the specified action will pass the filter.
//
// Possible values:
//   "CAPTURE"
//   "LOG"
func (c *DebuggerDebuggeesBreakpointsListCall) ActionValue(actionValue string) *DebuggerDebuggeesBreakpointsListCall {
	c.opt_["action.value"] = actionValue
	return c
}

// IncludeAllUsers sets the optional parameter "includeAllUsers": When
// set to true the response includes the list of breakpoints set by any
// user, otherwise only breakpoints set by the caller.
func (c *DebuggerDebuggeesBreakpointsListCall) IncludeAllUsers(includeAllUsers bool) *DebuggerDebuggeesBreakpointsListCall {
	c.opt_["includeAllUsers"] = includeAllUsers
	return c
}

// IncludeInactive sets the optional parameter "includeInactive": When
// set to true the response includes active and inactive breakpoints,
// otherwise only active breakpoints are returned.
func (c *DebuggerDebuggeesBreakpointsListCall) IncludeInactive(includeInactive bool) *DebuggerDebuggeesBreakpointsListCall {
	c.opt_["includeInactive"] = includeInactive
	return c
}

// StripResults sets the optional parameter "stripResults": When set to
// true the response breakpoints will be stripped of the results fields:
// stack_frames, evaluated_expressions and variable_table.
func (c *DebuggerDebuggeesBreakpointsListCall) StripResults(stripResults bool) *DebuggerDebuggeesBreakpointsListCall {
	c.opt_["stripResults"] = stripResults
	return c
}

// WaitToken sets the optional parameter "waitToken": A wait token that,
// if specified, blocks the call until the breakpoints list has changed,
// or a server selected timeout has expired. The value should be set
// from the last response to ListBreakpoints. The error code ABORTED is
// returned on wait timeout, which should be called again with the same
// wait_token.
func (c *DebuggerDebuggeesBreakpointsListCall) WaitToken(waitToken string) *DebuggerDebuggeesBreakpointsListCall {
	c.opt_["waitToken"] = waitToken
	return c
}

// Fields allows partial responses to be retrieved.
// See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse
// for more information.
func (c *DebuggerDebuggeesBreakpointsListCall) Fields(s ...googleapi.Field) *DebuggerDebuggeesBreakpointsListCall {
	c.opt_["fields"] = googleapi.CombineFields(s)
	return c
}

func (c *DebuggerDebuggeesBreakpointsListCall) Do() (*ListBreakpointsResponse, error) {
	var body io.Reader = nil
	params := make(url.Values)
	params.Set("alt", "json")
	if v, ok := c.opt_["action.value"]; ok {
		params.Set("action.value", fmt.Sprintf("%v", v))
	}
	if v, ok := c.opt_["includeAllUsers"]; ok {
		params.Set("includeAllUsers", fmt.Sprintf("%v", v))
	}
	if v, ok := c.opt_["includeInactive"]; ok {
		params.Set("includeInactive", fmt.Sprintf("%v", v))
	}
	if v, ok := c.opt_["stripResults"]; ok {
		params.Set("stripResults", fmt.Sprintf("%v", v))
	}
	if v, ok := c.opt_["waitToken"]; ok {
		params.Set("waitToken", fmt.Sprintf("%v", v))
	}
	if v, ok := c.opt_["fields"]; ok {
		params.Set("fields", fmt.Sprintf("%v", v))
	}
	urls := googleapi.ResolveRelative(c.s.BasePath, "v2/debugger/debuggees/{debuggeeId}/breakpoints")
	urls += "?" + params.Encode()
	req, _ := http.NewRequest("GET", urls, body)
	googleapi.Expand(req.URL, map[string]string{
		"debuggeeId": c.debuggeeId,
	})
	req.Header.Set("User-Agent", c.s.userAgent())
	res, err := c.s.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer googleapi.CloseBody(res)
	if err := googleapi.CheckResponse(res); err != nil {
		return nil, err
	}
	var ret *ListBreakpointsResponse
	if err := json.NewDecoder(res.Body).Decode(&ret); err != nil {
		return nil, err
	}
	return ret, nil
	// {
	//   "description": "Lists all breakpoints of the debuggee that the user has access to.",
	//   "httpMethod": "GET",
	//   "id": "clouddebugger.debugger.debuggees.breakpoints.list",
	//   "parameterOrder": [
	//     "debuggeeId"
	//   ],
	//   "parameters": {
	//     "action.value": {
	//       "description": "Only breakpoints with the specified action will pass the filter.",
	//       "enum": [
	//         "CAPTURE",
	//         "LOG"
	//       ],
	//       "location": "query",
	//       "type": "string"
	//     },
	//     "debuggeeId": {
	//       "description": "The debuggee id to list breakpoint from.",
	//       "location": "path",
	//       "required": true,
	//       "type": "string"
	//     },
	//     "includeAllUsers": {
	//       "description": "When set to true the response includes the list of breakpoints set by any user, otherwise only breakpoints set by the caller.",
	//       "location": "query",
	//       "type": "boolean"
	//     },
	//     "includeInactive": {
	//       "description": "When set to true the response includes active and inactive breakpoints, otherwise only active breakpoints are returned.",
	//       "location": "query",
	//       "type": "boolean"
	//     },
	//     "stripResults": {
	//       "description": "When set to true the response breakpoints will be stripped of the results fields: stack_frames, evaluated_expressions and variable_table.",
	//       "location": "query",
	//       "type": "boolean"
	//     },
	//     "waitToken": {
	//       "description": "A wait token that, if specified, blocks the call until the breakpoints list has changed, or a server selected timeout has expired. The value should be set from the last response to ListBreakpoints. The error code ABORTED is returned on wait timeout, which should be called again with the same wait_token.",
	//       "location": "query",
	//       "type": "string"
	//     }
	//   },
	//   "path": "v2/debugger/debuggees/{debuggeeId}/breakpoints",
	//   "response": {
	//     "$ref": "ListBreakpointsResponse"
	//   },
	//   "scopes": [
	//     "https://www.googleapis.com/auth/cloud-platform",
	//     "https://www.googleapis.com/auth/cloud_debugger"
	//   ]
	// }

}

// method id "clouddebugger.debugger.debuggees.breakpoints.set":

type DebuggerDebuggeesBreakpointsSetCall struct {
	s          *Service
	debuggeeId string
	breakpoint *Breakpoint
	opt_       map[string]interface{}
}

// Set: Sets the breakpoint to the debuggee.
func (r *DebuggerDebuggeesBreakpointsService) Set(debuggeeId string, breakpoint *Breakpoint) *DebuggerDebuggeesBreakpointsSetCall {
	c := &DebuggerDebuggeesBreakpointsSetCall{s: r.s, opt_: make(map[string]interface{})}
	c.debuggeeId = debuggeeId
	c.breakpoint = breakpoint
	return c
}

// Fields allows partial responses to be retrieved.
// See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse
// for more information.
func (c *DebuggerDebuggeesBreakpointsSetCall) Fields(s ...googleapi.Field) *DebuggerDebuggeesBreakpointsSetCall {
	c.opt_["fields"] = googleapi.CombineFields(s)
	return c
}

func (c *DebuggerDebuggeesBreakpointsSetCall) Do() (*SetBreakpointResponse, error) {
	var body io.Reader = nil
	body, err := googleapi.WithoutDataWrapper.JSONReader(c.breakpoint)
	if err != nil {
		return nil, err
	}
	ctype := "application/json"
	params := make(url.Values)
	params.Set("alt", "json")
	if v, ok := c.opt_["fields"]; ok {
		params.Set("fields", fmt.Sprintf("%v", v))
	}
	urls := googleapi.ResolveRelative(c.s.BasePath, "v2/debugger/debuggees/{debuggeeId}/breakpoints/set")
	urls += "?" + params.Encode()
	req, _ := http.NewRequest("POST", urls, body)
	googleapi.Expand(req.URL, map[string]string{
		"debuggeeId": c.debuggeeId,
	})
	req.Header.Set("Content-Type", ctype)
	req.Header.Set("User-Agent", c.s.userAgent())
	res, err := c.s.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer googleapi.CloseBody(res)
	if err := googleapi.CheckResponse(res); err != nil {
		return nil, err
	}
	var ret *SetBreakpointResponse
	if err := json.NewDecoder(res.Body).Decode(&ret); err != nil {
		return nil, err
	}
	return ret, nil
	// {
	//   "description": "Sets the breakpoint to the debuggee.",
	//   "httpMethod": "POST",
	//   "id": "clouddebugger.debugger.debuggees.breakpoints.set",
	//   "parameterOrder": [
	//     "debuggeeId"
	//   ],
	//   "parameters": {
	//     "debuggeeId": {
	//       "description": "The debuggee id to set the breakpoint to.",
	//       "location": "path",
	//       "required": true,
	//       "type": "string"
	//     }
	//   },
	//   "path": "v2/debugger/debuggees/{debuggeeId}/breakpoints/set",
	//   "request": {
	//     "$ref": "Breakpoint"
	//   },
	//   "response": {
	//     "$ref": "SetBreakpointResponse"
	//   },
	//   "scopes": [
	//     "https://www.googleapis.com/auth/cloud-platform",
	//     "https://www.googleapis.com/auth/cloud_debugger"
	//   ]
	// }

}
