# MI-004 — Subtract matched central-cut operators before taking their trace norm

**Evidence level:** supported; the central-collar estimate below is proved in its stated model.

On the fixed collar slab `(-R,R) x S^1` with metric `dr^2+L^2 cosh^2(r)dtheta^2` and Dirichlet outer boundary, define `G_L=(Delta_L+1)^-1-(Delta_L^cut+1)^-1`. Use the constant-density unitary to compare different lengths on one Hilbert space. Each absolute recoupling satisfies `||G_L||_1 >= c_R>0` as `L -> 0`, but for `L'=e^t L`, `|t|<=t_0`, [PF-173](../../findings/PF-173-relative-central-recoupling-is-trace-summable.md) proves

\[
P_0(G_{L'}-G_L)P_0=0,\qquad
\|G_{L'}-G_L\|_1\le C_{R,t_0}|t|L^2.
\]

The order-one channel is the common angular zero mode; it cancels exactly in the relative operator. Estimating `||G_{L'}||_1+||G_L||_1` first destroys the useful `|t|L^2` factor. The resulting relative corrections are trace-summable over the complete matched short-core family.

This is an orthogonal central-collar model, not the full uncut surface. Its artificial outer Dirichlet boundaries have not disappeared. It cannot imply a trace-class first relative resolvent for the genuinely non-isometric full two-dimensional pair; that overclaim is explicitly excluded in PF-173. The separate physical reassembly question is the normalized mixed response in [MI-008](MI-008-complete-cut-transmission-needs-extension-mass-not-only-boundary-impedance.md), not a failure of this local cancellation.
