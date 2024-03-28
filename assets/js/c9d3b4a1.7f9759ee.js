"use strict";(self.webpackChunkwebsite=self.webpackChunkwebsite||[]).push([[9202],{16956:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>o,contentTitle:()=>i,default:()=>d,frontMatter:()=>a,metadata:()=>c,toc:()=>l});var s=n(85893),r=n(11151);const a={sidebar_label:"utils",title:"agentchat.utils"},i=void 0,c={id:"reference/agentchat/utils",title:"agentchat.utils",description:"gather\\usage\\summary",source:"@site/docs/reference/agentchat/utils.md",sourceDirName:"reference/agentchat",slug:"/reference/agentchat/utils",permalink:"/autogen/docs/reference/agentchat/utils",draft:!1,unlisted:!1,editUrl:"https://github.com/microsoft/autogen/edit/main/website/docs/reference/agentchat/utils.md",tags:[],version:"current",frontMatter:{sidebar_label:"utils",title:"agentchat.utils"},sidebar:"referenceSideBar",previous:{title:"user_proxy_agent",permalink:"/autogen/docs/reference/agentchat/user_proxy_agent"},next:{title:"abstract_cache_base",permalink:"/autogen/docs/reference/cache/abstract_cache_base"}},o={},l=[{value:"gather_usage_summary",id:"gather_usage_summary",level:3},{value:"parse_tags_from_content",id:"parse_tags_from_content",level:3}];function h(e){const t={a:"a",audio:"audio",code:"code",em:"em",h3:"h3",li:"li",p:"p",pre:"pre",strong:"strong",ul:"ul",...(0,r.a)(),...e.components};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(t.h3,{id:"gather_usage_summary",children:"gather_usage_summary"}),"\n",(0,s.jsx)(t.pre,{children:(0,s.jsx)(t.code,{className:"language-python",children:"def gather_usage_summary(\n        agents: List[Agent]) -> Tuple[Dict[str, any], Dict[str, any]]\n"})}),"\n",(0,s.jsx)(t.p,{children:"Gather usage summary from all agents."}),"\n",(0,s.jsxs)(t.p,{children:[(0,s.jsx)(t.strong,{children:"Arguments"}),":"]}),"\n",(0,s.jsxs)(t.ul,{children:["\n",(0,s.jsxs)(t.li,{children:[(0,s.jsx)(t.code,{children:"agents"})," - (list): List of agents."]}),"\n"]}),"\n",(0,s.jsxs)(t.p,{children:[(0,s.jsx)(t.strong,{children:"Returns"}),":"]}),"\n",(0,s.jsxs)(t.ul,{children:["\n",(0,s.jsxs)(t.li,{children:[(0,s.jsx)(t.code,{children:"tuple"})," - (total_usage_summary, actual_usage_summary)"]}),"\n"]}),"\n",(0,s.jsxs)(t.p,{children:[(0,s.jsx)(t.strong,{children:"Example"}),":"]}),"\n",(0,s.jsx)(t.pre,{children:(0,s.jsx)(t.code,{className:"language-python",children:'total_usage_summary = {\n    "total_cost": 0.0006090000000000001,\n    "gpt-35-turbo": {\n            "cost": 0.0006090000000000001,\n            "prompt_tokens": 242,\n            "completion_tokens": 123,\n            "total_tokens": 365\n    }\n}\n'})}),"\n",(0,s.jsxs)(t.p,{children:[(0,s.jsx)(t.strong,{children:"Notes"}),":"]}),"\n",(0,s.jsxs)(t.p,{children:[(0,s.jsx)(t.code,{children:"actual_usage_summary"})," follows the same format.\nIf none of the agents incurred any cost (not having a client), then the total_usage_summary and actual_usage_summary will be ",(0,s.jsx)(t.code,{children:"{'total_cost': 0}"}),"."]}),"\n",(0,s.jsx)(t.h3,{id:"parse_tags_from_content",children:"parse_tags_from_content"}),"\n",(0,s.jsx)(t.pre,{children:(0,s.jsx)(t.code,{className:"language-python",children:"def parse_tags_from_content(\n    tag: str,\n    content: Union[str, List[Dict[str,\n                                  Any]]]) -> List[Dict[str, Dict[str, str]]]\n"})}),"\n",(0,s.jsx)(t.p,{children:"Parses HTML style tags from message contents."}),"\n",(0,s.jsx)(t.p,{children:"The parsing is done by looking for patterns in the text that match the format of HTML tags. The tag to be parsed is\nspecified as an argument to the function. The function looks for this tag in the text and extracts its content. The\ncontent of a tag is everything that is inside the tag, between the opening and closing angle brackets. The content\ncan be a single string or a set of attribute-value pairs."}),"\n",(0,s.jsxs)(t.p,{children:[(0,s.jsx)(t.strong,{children:"Examples"}),":"]}),"\n",(0,s.jsxs)(t.p,{children:["<img ",(0,s.jsx)(t.a,{href:"http://example.com/image.png%3E",children:"http://example.com/image.png>"}),' -> [{"tag": "img", "attr": {"src": "',(0,s.jsx)(t.a,{href:"http://example.com/image.png",children:"http://example.com/image.png"}),'"}, "match": re.Match}]\n',(0,s.jsx)(t.audio,{text:"Hello I'm a robot",prompt:"whisper",children:" ->"})]}),"\n",(0,s.jsxs)(t.ul,{children:["\n",(0,s.jsxs)(t.li,{children:[(0,s.jsx)(t.code,{children:'[{"tag"'}),' - "audio", "attr": {"text": "Hello I\'m a robot", "prompt": "whisper"}, "match": re.Match}]']}),"\n"]}),"\n",(0,s.jsxs)(t.p,{children:[(0,s.jsx)(t.strong,{children:"Arguments"}),":"]}),"\n",(0,s.jsxs)(t.ul,{children:["\n",(0,s.jsxs)(t.li,{children:[(0,s.jsx)(t.code,{children:"tag"})," ",(0,s.jsx)(t.em,{children:"str"})," - The HTML style tag to be parsed."]}),"\n",(0,s.jsxs)(t.li,{children:[(0,s.jsx)(t.code,{children:"content"})," ",(0,s.jsx)(t.em,{children:"Union[str, List[Dict[str, Any]]]"})," - The message content to parse. Can be a string or a list of content\nitems."]}),"\n"]}),"\n",(0,s.jsxs)(t.p,{children:[(0,s.jsx)(t.strong,{children:"Returns"}),":"]}),"\n",(0,s.jsx)(t.p,{children:"List[Dict[str, str]]: A list of dictionaries, where each dictionary represents a parsed tag. Each dictionary\ncontains three key-value pairs: 'type' which is the tag, 'attr' which is a dictionary of the parsed attributes,\nand 'match' which is a regular expression match object."}),"\n",(0,s.jsxs)(t.p,{children:[(0,s.jsx)(t.strong,{children:"Raises"}),":"]}),"\n",(0,s.jsxs)(t.ul,{children:["\n",(0,s.jsxs)(t.li,{children:[(0,s.jsx)(t.code,{children:"ValueError"})," - If the content is not a string or a list."]}),"\n"]})]})}function d(e={}){const{wrapper:t}={...(0,r.a)(),...e.components};return t?(0,s.jsx)(t,{...e,children:(0,s.jsx)(h,{...e})}):h(e)}},11151:(e,t,n)=>{n.d(t,{Z:()=>c,a:()=>i});var s=n(67294);const r={},a=s.createContext(r);function i(e){const t=s.useContext(a);return s.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function c(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(r):e.components||r:i(e.components),s.createElement(a.Provider,{value:t},e.children)}}}]);