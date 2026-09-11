---
id: CLUE-prime-flute-variable-corridor-reservoir-weyl-mass
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-228-flat-corridor-dressing-makes-inverse-seam-multiplicity-weak-trace-compatible.md
  - research/prime_flute/findings/PF-229-frozen-serial-schur-completion-preserves-flat-corridor-cut-scale.md
  - research/prime_flute/findings/PF-279-variable-scalar-schur-reservoirs-can-erase-local-corridor-cut-gain.md
  - research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Does canonical tail mass prevent scalar reservoir amplification of a dressed cut?

## Observation

PF-229 compares the full half-chain cut norm with isolated transmission only when the same normalized corridor edge is repeated. Its rank-one calculation retains the norms of the two geometric tails; those norms need not stay calibrated to the cut edge in a variable chain. This clue isolates that issue with exact PF-228 corridor coefficients, rather than arbitrary positive matrices or a new channel-multiplicity construction. It does not challenge PF-229's frozen theorem.

The following algebraic control is provided for independent reconstruction, not as a new canonical finding. Use one common seam halfwidth `w` and one common tangential parameter `mu>=1`. For an edge of length `ell`, set

\[
t=\tanh(\mu w),\quad
m(\ell)=\frac{\tanh(\mu\ell/2)}{t},\quad
c(\ell)=\frac{\operatorname{csch}(\mu\ell)}{t},\quad
K_\ell=\begin{pmatrix}m+c&-c\\-c&m+c\end{pmatrix}.
\]

Every edge form is positive. Assemble `M=I+sum_edges K_ell` on the scalar bi-infinite chain. Take the edge `(0,1)` to have length `S`, with `mu S=1`, and every other edge to have length `kw`, for fixed `k>0`. Write `epsilon=w/S=mu w`, `m_1=m(S)`, `c_1=c(S)`, `m_0=m(kw)`, and `c_0=c(kw)`. The family can also have `S` tend to zero; the calculation depends only on `epsilon` and `k`.

Define

\[
H_0=1+2m_0,\qquad R_0=\sqrt{H_0(H_0+4c_0)},\qquad
r_0=\frac{2c_0}{H_0+2c_0+R_0},\qquad
\alpha=m_1+\frac{1+R_0}{2}.
\]

For each fixed `epsilon>0`, eliminate the two constant background half-chains. Their decaying solutions are `r_0^j`. The remaining two-boundary matrix is `alpha I+c_1 L_2`, so its off-diagonal inverse entry is `c_1/[alpha(alpha+2c_1)]`. The full cut `X=1_{j>=1} M^{-1}1_{j<=0}` is rank one, but each extension vector has squared norm `(1-r_0^2)^{-1}`. Thus the candidate exact certificate is

\[
\boxed{\|X\|=\frac{c_1}{\alpha(\alpha+2c_1)(1-r_0^2)}},
\qquad
x_{\rm loc}=\frac{c_1}{(1+m_1)(1+m_1+2c_1)}.
\]

The Schur diagonal follows directly from `1+m_0+c_0(1-r_0)=(1+R_0)/2`; this counts the incident edge masses and distinguishes the full cut from its nearest-neighbor entry.

Put `a=tanh(1/2)`, `b=csch(1)`, and `q=sqrt((k+1)/k)`. As `epsilon` tends to zero,

\[
m_0\to k/2,\quad c_0\sim\frac1{k\epsilon^2},\quad
\alpha\sim\frac{a+q}{\epsilon},\quad
1-r_0^2\sim2\epsilon\sqrt{k(k+1)}.
\]

Consequently

\[
x_{\rm loc}\sim\epsilon\frac{b}{a(a+2b)},\qquad
\boxed{\|X\|\longrightarrow
\frac{b}{2\sqrt{k(k+1)}(a+q)(a+q+2b)}>0.}
\]

The boundary Green entry still has order `epsilon`; extension into the two long background tails removes that gain in the full cut norm. No tangential mode mixing or failure of `M>=I` is involved. For `k=4`, the limiting constant is approximately `0.01834455759`.

There is a necessary incidence refinement: the canonical scale uses two consecutive gaps, so an isolated large gap affects two neighboring corridor lengths. Replace both edges `(0,1)` and `(1,2)` by length `S`. After eliminating the same backgrounds the central matrix is

\[
B_3=\begin{pmatrix}
\alpha+c_1&-c_1&0\\
-c_1&1+2m_1+2c_1&-c_1\\
0&-c_1&\alpha+c_1
\end{pmatrix},\qquad G=B_3^{-1}.
\]

Across the first defect edge, the full cut norm is

\[
\|X_{\rm pair}\|^2=
\frac{|G_{10}|^2+|G_{20}|^2/(1-r_0^2)}{1-r_0^2}.
\]

Writing `p=a+q+b`, its limiting value is

\[
\frac{b^2}{4\sqrt{k(k+1)}\,p\big((a+b)p-b^2\big)}>0.
\]

Thus merely requiring two adjacent exceptional corridor lengths does not remove the scalar mechanism. This is still not a realization by consecutive primes.

## Research question

Which actual-PF hypothesis controls the mass of the left and right Poisson extensions relative to the cut corridor, and does that control need to hold for the whole cut or only after the physical `P/H` projections?

A precise scalar interface is available. For a fixed positive Jacobi precision `K`, vary only the resolvent shift in `M_eta=K+eta I`; keep its corridor coefficients and tangential parameter fixed. Let `A_L(eta),A_R(eta)` be the two half-chain compressions including the cut edge's diagonal terms, and let `c` be its crossing conductance. With endpoint vectors `e_L,e_R`, put

\[
\beta_L(\eta)=\langle e_L,A_L(\eta)^{-1}e_L\rangle^{-1},\qquad
\beta_R(\eta)=\langle e_R,A_R(\eta)^{-1}e_R\rangle^{-1}.
\]

Block inversion and differentiation of a resolvent give

\[
\boxed{\|1_R M_\eta^{-1}1_L\|
=\frac{c\sqrt{\beta_L'(\eta)\beta_R'(\eta)}}
{\beta_L(\eta)\beta_R(\eta)-c^2}.}
\]

Indeed, the harmonic extension with endpoint value one has squared norm `beta_L'` or `beta_R'`. The missing information is therefore not just the two boundary impedances; it is also their spectral derivatives, equivalently the extension Gram forms. Seek a useful matrix/operator analogue that retains these forms in the actual boundary-energy spaces, rather than replacing them prematurely by scalar norms.

## Why it may matter

This is a specific obstruction to a uniform extrapolation of PF-229 to arbitrary variable scalar corridors. It suggests a concrete replacement interface: control tail-extension mass, or prove that the actual mixed projections remove its amplification. Such a result could change which one-cut bound is worth demanding before PF-222 reassembly. It is not another proof that compactness or a universal resolvent cap is insufficient.

The ingredients are classical Jacobi/Weyl theory and Schur elimination, not claimed new mathematics: Gerald Teschl, *Jacobi Operators and Completely Integrable Nonlinear Lattices*, AMS Mathematical Surveys and Monographs 72 (2000); Florian Dörfler and Francesco Bullo, *Kron Reduction of Graphs With Applications to Electrical Networks*, IEEE Transactions on Circuits and Systems I 60 (2013), 150–163, DOI `10.1109/TCSI.2012.2215780`, arXiv `1102.2950`. The unresolved contribution sought here is an actual-PF tail-mass/projection test, not novelty of the scalar formula.

## Decisive test

First reconstruct the one-defect and paired-defect formulas directly, with the precise edge-mass convention above. A reproducible finite check retains homogeneous Dirichlet exterior diagonals and chooses each background half-chain length `N=ceil(12/(1-r_0))`. Solving the tridiagonal system for the two endpoint delta vectors gives the cut norm from the rank-one row/column factorization. At `k=4` and `epsilon=0.1,0.03,0.01`, finite systems with `68,192,550` total nodes agreed with the infinite one-defect formula to relative error below `1e-8`; 70-digit evaluation also confirms the displayed asymptotics. These are diagnostic checks, not a proof substitute or an independent review.

Then identify whether canonical neighboring pant forms can support the required extended low-impedance backgrounds. Either prove a source/geometric bound on the corresponding extension Gram forms, or construct the mechanism within the canonical geometry. Match `s_n` to the two-gap scale and `w_n` to the natural seam width; do not assume arbitrarily long fixed small-gap prime patterns exist. An increasing background scale and the number of available neighboring modules must be analyzed together. A constructive Gram bound and an admissible reservoir search are genuinely complementary tests of the same interface.

Crucially retain the physical `P/H` split. The control above is an unprojected cut; if the same scalar mode has the same low/high classification in every module, its mixed `P[D,E_j]H` contribution can vanish identically. Determine whether physical projections suppress the enlarged tails, preserve them, or require genuine intermode coupling. Never manufacture mixing by changing coordinates while leaving the physical projectors incorrectly fixed.

Finally charge any surviving amplification to the actual reciprocal-prime jump and its frequency population. Failure of an unprojected `O(w_j/s_j)` bound does not imply that the weighted projected series fails weak trace class; a weaker bound with a compensating population or source-frequency estimate may suffice. Do not replace the nested cuts by an orthogonal direct sum.

## Evidence boundary

PF-279 now records the scalar one-defect and paired-defect reservoir calculation, together with the exact Weyl-derivative/extension-mass identity, as a canonical matched-control theorem. Its Jacobi/Weyl and Schur/Kron ingredients are classical; no general novelty is claimed for them.

What remains unproved is precisely the actual-PF transfer. No admissible consecutive-prime reservoir, actual hyperbolic-pant amplification, surviving mixed `P/H` flux, or weak-Schatten failure has been established. The paired-defect control enforces only a local overlap pattern, not arithmetic realizability. No claim about wave operators, prime/clone separation, or RH follows. The existing accepted weak-trace clue retains its scope and disposition.

## Research disposition

The clue is `accepted`. The scalar mechanism survived independent reconstruction and a prior-art audit and is now persisted as PF-279. The live question is no longer whether the scalar algebra is real, but whether the canonical prime-flute boundary-energy problem controls the operator-valued analogues of `beta_L'` and `beta_R'`, or whether physical `P/H` projection and arithmetic incidence suppress the reservoir before PF-222's reciprocal-prime nested reassembly. A positive Gram bound would kill this matched control for the actual geometry; a realizable projected reservoir would force a different weak-trace reassembly currency.