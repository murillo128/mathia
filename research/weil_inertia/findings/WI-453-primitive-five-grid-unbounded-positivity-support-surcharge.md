# WI-453 — A fixed five-grid primitive family has unbounded nonnegative Fourier-support surcharge

**Status:** EXACT-DERIVED + CLASSICAL-CYCLOTOMIC-REDUCTION + EXACT-SUPPORT-SEPARATION + WANG-CLASS-SPECIALIZATION + NON-RH + NO-PRIORITY-CLAIM

**Local dependencies:** WI-450 (Fourier support and Wang smooth-square smoothing), WI-451 (commensurate two-grid overlap), WI-452 (finite-grid polynomial criterion and the four-grid coefficient certificate).

**Prior-art boundary:** Kolountzakis--Papageorgiou (2022, arXiv:2106.11701v2) study simultaneous lattice tilings and support bounds; Steinberger (2012), Kepka--Korbelář (2012), and Tan--Zhang (2026 preprint) study nonnegative cyclotomic multiples and their support diameter. The following residue-class amplification is elementary polynomial algebra applied to WI-452's exact certificate. No claim of a new general tiling theorem or literature priority is made.

## Claim: exact amplification under common period dilation

For a finite set \(M\subset\mathbb N\), define
\[
S_m(z)=1+z+\cdots+z^{m-1},\quad
Q_M(z)=\operatorname{lcm}_{m\in M}S_m(z),\quad
D_M=\deg Q_M,
\]
and let \(d_+(Q)\) denote the smallest degree of a nonzero real-coefficient polynomial with **all coefficients nonnegative** divisible by \(Q\). Put \(\Delta_M=d_+(Q_M)-D_M\ge0\). For every positive integer \(t\), with \(tM=\{tm:m\in M\}\), one has
\[
\boxed{Q_{tM}(z)=S_t(z)Q_M(z^t)}, \qquad
\boxed{D_{tM}=t(D_M+1)-1},                                   \tag{1}
\]
and the exact positivity-degree identity
\[
\boxed{d_+(Q_{tM})=t(d_+(Q_M)+1)-1},\qquad
\boxed{\Delta_{tM}=t\Delta_M}.                              \tag{2}
\]
Here the unit of polynomial degree is an \(h\)-cell; equation (2) by itself is just a common rescaling of all periods, not yet a primitive-family separation.

Now let \(r\) be prime and assume \(r\nmid t\prod_{m\in M}m\). Adjoining the genuinely new period \(r\) gives \(M_{t,r}=tM\cup\{r\}\). Since \(\Phi_r=S_r\) is coprime to \(Q_{tM}\),
\[
Q_{M_{t,r}}(z)=S_r(z)S_t(z)Q_M(z^t),\qquad
D_{M_{t,r}}=t(D_M+1)+r-2.                                   \tag{3}
\]
Moreover,
\[
t(d_+(Q_M)+1)-1
\ \le\ d_+(Q_{M_{t,r}})
\ \le\ t(d_+(Q_M)+1)+r-2,
\]
so
\[
\boxed{t\Delta_M-(r-1)\ \le\
\Delta_{M_{t,r}}\ \le\ t\Delta_M}.                          \tag{4}
\]
The added period is not a redundant Fourier grid: its primitive \(r\)-th roots are absent from the original grid divisor.

## Proof of the degree identities

The identity \(S_{tm}(z)=S_t(z)S_m(z^t)\) and the fact that substitution \(z\mapsto z^t\) preserves polynomial gcd/lcm up to monic normalization establish (1). Its degree statement follows immediately.

Let \(P(z)\) be any nonzero polynomial with nonnegative real coefficients divisible by \(S_t(z)Q_M(z^t)\). Split its coefficients into \(t\) residue polynomials
\[
P_a(w)=\sum_{j\ge0}[z^{tj+a}]P(z)\,w^j,\qquad 0\le a<t.
\]
Because \(Q_M(z^t)\mid P(z)\), one has \(Q_M(w)\mid P_a(w)\) for **every** \(a\). Because \(S_t(z)\mid P(z)\), evaluating at the nontrivial \(t\)-th roots of unity and inverting the finite Fourier transform gives
\[
P_0(1)=P_1(1)=\cdots=P_{t-1}(1)=P(1)/t>0.
\]
Thus all \(P_a\) are nonzero nonnegative multiples of \(Q_M\), each of degree at least \(d_+(Q_M)\). In particular, the residue \(a=t-1\) forces
\(\deg P\ge t\,d_+(Q_M)+t-1\).
Conversely if \(A(w)\) is a least-degree nonnegative multiple of \(Q_M\), then \(S_t(z)A(z^t)\) is a nonnegative multiple of \(Q_{tM}\) of exactly that degree. This proves (2), including \(t=1\).

For (3), any root of \(S_r=\Phi_r\) has exact order \(r\), which cannot divide any \(tm\) under the stated hypothesis. Therefore \(S_r\) is coprime to \(Q_{tM}\) and degrees add. Every nonnegative multiple of \(Q_{M_{t,r}}\) is a nonnegative multiple of \(Q_{tM}\), giving the first inequality in (4). Multiplying a minimizing positive multiple of \(Q_{tM}\) by \(S_r\), which has nonnegative coefficients and degree \(r-1\), gives the second inequality. No assumption about uniqueness of a minimizing multiple is used.

## Explicit primitive five-grid consequence

Use WI-452's exact four-grid certificate
\[
M_4=\{14,21,30,35\},\qquad
D_{M_4}=77,\qquad d_+(Q_{M_4})=78.
\]
Fix \(r=11\), and for any positive integer \(t\) with \(11\nmid t\) set
\[
\mathcal M_t=\{14t,21t,30t,35t,11\}.                         \tag{5}
\]
The five periods are distinct, **no one divides another**, and their gcd is \(1\). The \(11\)-grid adds an independent cyclotomic constraint (not an independent *irrational* period). Equations (3)--(4) yield
\[
\boxed{D_{\mathcal M_t}=78t+9},\qquad
\boxed{79t-1\le d_+(Q_{\mathcal M_t})\le79t+9},               \tag{6}
\]
and hence
\[
\boxed{t-10\le\Delta_{\mathcal M_t}\le t}.                   \tag{7}
\]
In particular the **additive positivity surcharge in primitive \(h\)-cells is unbounded with only five nonredundant commensurate reciprocal grids**, despite their integer gcd remaining exactly \(1\).

Using WI-452's sharp interval-support theorem, for the actual periods \(\{mh:m\in\mathcal M_t\}\) the optimal signed and nonnegative normalized integrable support lengths satisfy
\[
L_{\rm signed}=(78t+10)h,\qquad
79th\le L_{\rm nonnegative}\le(79t+10)h.
\]
Thus \(L_{\rm nonnegative}-L_{\rm signed}\in[(t-10)h,th]\) and
\[
\lim_{\substack{t\to\infty\\11\nmid t}}
\frac{L_{\rm nonnegative}}{L_{\rm signed}}=\frac{79}{78}.
\tag{8}
\]
For Wang's even smooth-square class in an open window of length \(\lambda\), exact feasibility remains the strict WI-452 criterion
\(h(d_+(Q_{\mathcal M_t})+1)<\lambda\). Equation (6) implies **impossibility** when \(\lambda\le79th\) and **existence** when \(\lambda>(79t+10)h\); it does *not* determine the transition within that width-\(10h\) interval.

For a concrete nondegenerate case \(t=12\), the periods are
\(\{168,252,360,420,11\}h\); signed support is \(946h\), while positive support is at least \(948h\) and at most \(958h\). These thresholds can fit the Wang range \(0<\lambda\le1\) by taking sufficiently small \(h\).

## Scope, prior art, and decisive boundaries

This is a source-specific corollary of WI-452's polynomial support theorem and its explicit \(M_4\) coefficient certificate, not a new arithmetic property of zeta. The finite Fourier transform argument is elementary, and existing nonnegative cyclotomic-multiple/tiling literature is the appropriate comparison class. The additive gap in \(h\)-cells is not evidence of arbitrarily large relative overhead: in (8) the relative excess approaches only \(1/78\), and fixing an admissible support window requires rescaling \(h\) as \(t\) increases.

The proof critically uses the **complete** reciprocal Fourier-zero grids, coefficientwise nonnegativity, and the extra \(\Phi_{11}\) factor with \(11\nmid t\). If \(11\mid t\), that factor may already occur and (3)--(7) cannot be asserted unchanged. This is an enclosing-interval result, not a lower bound for the measure of a disconnected support, and the signed \(Q\) density is not Wang-admissible. The source-independent Fourier constraints are freely prescribed; no argument here derives them from zeta zeros or excludes even a single off-critical zero. The unresolved RH-facing step remains an independently justified source-to-individual-defect bridge.
