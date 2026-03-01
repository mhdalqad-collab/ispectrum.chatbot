"use client";

import { useState } from "react";
import { postJSON } from "../../lib/api";

type Role = "user" | "assistant";
type Msg = { role: Role; content: string };

export default function ChatPage() {
  const [system, setSystem] = useState("You are a helpful assistant for business tasks. Be concise and practical.");
  const [input, setInput] = useState("");
  const [msgs, setMsgs] = useState<Msg[]>([]);
  const [busy, setBusy] = useState(false);

  const quick = [
    "Summarize this text clearly",
    "Write a professional email reply",
    "Create a short pitch for my product",
    "Suggest steps to solve this problem",
  ];

  async function send(text?: string) {
    const message = (text ?? input).trim();
    if (!message || busy) return;

    const nextMsgs: Msg[] = [...msgs, { role: "user", content: message }];
    setMsgs(nextMsgs);
    setInput("");
    setBusy(true);

    try {
      const history: Msg[] = nextMsgs.slice(0, -1).map((m) => ({ role: m.role, content: m.content }));
      const out = await postJSON<{ response: string }>("/v1/chat", { message, system, history });
      setMsgs([...nextMsgs, { role: "assistant", content: out.response }]);
    } catch (e: any) {
      setMsgs([...nextMsgs, { role: "assistant", content: `Sorry — I couldn't reach the server. (${e.message})` }]);
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="card">
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", gap: 12, flexWrap: "wrap" }}>
        <h2 style={{ margin: 0 }}>Assistant</h2>
        <span className="small">Tip: press Enter to send</span>
      </div>
  
      <div className="hr" />
  
      <div className="label">Assistant behavior (optional)</div>
      <textarea className="textarea" value={system} onChange={(e) => setSystem(e.target.value)} />
  
      <div className="hr" />
  
      <div className="row">
        {quick.map((q) => (
          <button key={q} className="button secondary" onClick={() => send(q)} disabled={busy}>
            {q}
          </button>
        ))}
      </div>
  
      <div className="hr" />
  
      <div className="label">Conversation</div>
      <div className="chatBox">
        {msgs.length === 0 ? (
          <div className="small">Start by typing a message below.</div>
        ) : (
          msgs.map((m, i) => (
            <div key={i} className="msgRow">
              <div className={`msg ${m.role}`}>{m.content}</div>
            </div>
          ))
        )}
      </div>
  
      <div className="hr" />
  
      <div className="row">
        <input
          className="input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              send();
            }
          }}
        />
        <button className="button" onClick={() => send()} disabled={busy}>
          {busy ? "Thinking..." : "Send"}
        </button>
      </div>
    </div>
  );
}