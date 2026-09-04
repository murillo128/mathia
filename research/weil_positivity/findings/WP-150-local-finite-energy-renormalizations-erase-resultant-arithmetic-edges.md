# WP-150 — Local finite-energy renormalizations erase every fixed resultant arithmetic edge

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + CYCLOTOMIC-RESULTANT + GRAPH-DIRICHLET + DIAGONAL-CONGRUENCE + NORMALIZED-LAPLACIAN + FINITE-CORE-COLLAPSE + SELECTOR-ERASURE + MATCHED-FINITE-PRIME-CONTROL + PRIOR-ART-AUDITED`

## Claim

`WP-148` found a canonical positive completion of the normalized Prime-Circle resultant kernel on every finite shell set: its weighted graph Laplacian. `WP-149` then showed that the unchanged all-prime Dirichlet energy collapses much more severely than an ordinary infinite-degree graph: spectator-prime bypasses force zero effective resistance on every arithmetic edge, so every finite-energy function is constant and no faithful change of ambient vertex measure rescues the same form.

A natural remaining escape is to **renormalize the positive cutoff forms themselves** before taking the all-prime limit. The standard symmetric normalized Laplacian is the most canonical example, but one can allow any positive vertex-local diagonal congruence.

That entire local class has a sharp obstruction. Let `F_i` be any increasing finite exhaustion of the shell set, let

\[
L_i=D_i-J_i\succeq0
\tag{1}
\]

be the resultant graph Laplacian on `F_i`, and let

\[
Q_i=R_iL_iR_i,\qquad
R_i=\operatorname{diag}(r_i(m)),\quad r_i(m)>0.
\tag{2}
\]

If the renormalization makes the energy of every fixed shell basis vector remain finite,

\[
\sup_i\langle \delta_m,Q_i\delta_m\rangle<\infty
\qquad\text{for every fixed }m,
\tag{3}
\]

then every fixed off-diagonal arithmetic coupling disappears:

\[
\boxed{
\langle\delta_m,Q_i\delta_n\rangle\longrightarrow0
\qquad(m\ne n).
}
\tag{4}
\]

If the basis energies themselves converge, every finite-support bilinear limit is therefore **diagonal**. In particular, the symmetric normalized resultant Laplacians converge on the fixed finite core `c_00` only in the bilinear-form sense to the identity form. They retain independent positivity but erase the prime-power selector that made the resultant kernel arithmetically relevant.

For the degree-power family `R_i=D_i^{-\alpha}` there is an exact trichotomy: `\alpha<1/2` leaves every fixed basis energy divergent, `\alpha=1/2` gives the universal identity finite-core limit, and `\alpha>1/2` gives the zero finite-core limit. Thus no vertex-local degree renormalization can simultaneously keep a nontrivial fixed arithmetic edge and make all fixed shell states have finite energy.

The result is deliberately a **finite-core theorem**, not a claim of strong operator convergence. Normalized adjacency mass can escape to shell indices tending to infinity. A surviving construction could therefore change the test-space identification with the cutoff, use a genuinely nonlocal interaction, or couple finite and archimedean sectors before taking the limit. What is closed is the canonical strategy of curing `WP-149` by local positive rescaling while expecting the original fixed-shell Weil selector to survive.

## 1. Resultant cutoff Laplacians

For distinct shell indices `m,n`, retain the normalized Prime-Circle resultant weight

\[
J_{m,n}
=
\frac{\log|\operatorname{Res}(\Phi_m,\Phi_n)|}
{\sqrt{\varphi(m)\varphi(n)}}\ge0.
\tag{5}
\]

By Apostol's cyclotomic-resultant theorem, this is nonzero exactly on prime-power ratios. On a finite shell set `F_i`, define

\[
d_i(m)=\sum_{\substack{n\in F_i\\n\ne m}}J_{m,n},
\qquad
D_i=\operatorname{diag}(d_i(m)),
\qquad
L_i=D_i-J_i.
\tag{6}
\]

Then

\[
\langle f,L_if\rangle
=
\frac12\sum_{m,n\in F_i}J_{m,n}|f_m-f_n|^2
\ge0.
\tag{7}
\]

Thus every `Q_i` in (2) is positive for the same independent finite graph-geometric reason:

\[
\langle f,Q_if\rangle
=
\langle R_if,L_iR_if\rangle
\ge0.
\tag{8}
\]

No RH input, zero divisor, Weil-positive kernel, or sign-forcing regularization is used here.

The all-prime obstruction begins with the exact fresh-prime edge derived in `WP-148`. For every fixed `m` and every prime `p\nmid m`,

\[
J_{m,mp}=\frac{\log p}{\sqrt{p-1}}.
\tag{9}
\]

Because an increasing exhaustion eventually contains any prescribed finite set of the vertices `mp`, equation (9) and divergence of the corresponding positive prime sum imply

\[
\boxed{d_i(m)\longrightarrow\infty}
\qquad\text{for every fixed shell }m.
\tag{10}
\]

This conclusion is exhaustion-independent. No special ordering by shell size is required.

## 2. Finite shell energy forces every local scale to zero

For a basis vector `\delta_m`, the diagonal congruence has the exact energy

\[
q_i(m)
:=
\langle\delta_m,Q_i\delta_m\rangle
=
r_i(m)^2d_i(m).
\tag{11}
\]

Assume only the minimal finite-core requirement (3). Combining it with (10) gives

\[
r_i(m)^2
=
\frac{q_i(m)}{d_i(m)}
\longrightarrow0,
\qquad
\boxed{r_i(m)\longrightarrow0}
\tag{12}
\]

for every fixed shell.

But the off-diagonal coefficient of the renormalized form is

\[
(Q_i)_{m,n}
=-r_i(m)r_i(n)J_{m,n}
\qquad(m\ne n).
\tag{13}
\]

For fixed `m,n`, the arithmetic coefficient `J_{m,n}` is independent of the cutoff. Equation (12) therefore gives (4) immediately.

This yields a useful dichotomy for every fixed nonzero resultant edge. If one demands

\[
\limsup_i
\big|\langle\delta_m,Q_i\delta_n\rangle\big|>0,
\qquad J_{m,n}>0,
\tag{14}
\]

then the basis energies at `m` and `n` cannot both remain bounded. In other words, **keeping a fixed arithmetic interaction and making every fixed shell finite-energy are mutually incompatible inside the entire vertex-local congruence class**.

The argument does not depend on monotonicity of the `r_i`, on a power law, or on selecting the degree normalization in advance. It uses only positivity by congruence, local diagonal scaling, and the exact all-prime degree divergence forced by the resultant weights.

## 3. Every finite-core limit is diagonal

Suppose more specifically that the individual basis energies converge,

\[
q_i(m)\longrightarrow q(m)<\infty
\qquad\text{for every fixed }m.
\tag{15}
\]

Let `f,g\in c_{00}` have common finite support contained in `S`. Once `S\subset F_i`,

\[
\langle f,Q_ig\rangle
=
\sum_{m\in S}q_i(m)\overline{f_m}g_m
-
\sum_{\substack{m,n\in S\\m\ne n}}
J_{m,n}r_i(m)r_i(n)\overline{f_m}g_n.
\tag{16}
\]

The second sum has finitely many fixed terms, and every one tends to zero by (12). Hence

\[
\boxed{
\langle f,Q_ig\rangle
\longrightarrow
\sum_m q(m)\overline{f_m}g_m.
}
\tag{17}
\]

So any convergent local finite-energy normalization forgets the resultant adjacency on fixed arithmetic states and leaves only a multiplication form. The prime-power support and the critical `\log p` amplitudes are precisely in the off-diagonal coefficients; they do not survive (17).

The conclusion remains true subsequentially when the `q_i(m)` are merely bounded: every finite-core cluster point is diagonal. Thus one cannot hide the arithmetic coupling in oscillatory choices of local normalization while retaining bounded energy on all fixed basis states.

## 4. The symmetric normalized Laplacian becomes the identity on the fixed core

The standard degree normalization chooses

\[
R_i=D_i^{-1/2}
\tag{18}
\]

on vertices of positive degree. For every fixed shell this is well-defined for all sufficiently large cutoffs, and

\[
\mathcal L_i
:=
D_i^{-1/2}L_iD_i^{-1/2}
=
I-D_i^{-1/2}J_iD_i^{-1/2}.
\tag{19}
\]

Its basis energies are identically one:

\[
\langle\delta_m,\mathcal L_i\delta_m\rangle=1.
\tag{20}
\]

For each fixed edge,

\[
(\mathcal L_i)_{m,n}
=-\frac{J_{m,n}}
{\sqrt{d_i(m)d_i(n)}}
\longrightarrow0.
\tag{21}
\]

Therefore for every fixed finitely supported `f,g`,

\[
\boxed{
\langle f,\mathcal L_i g\rangle
\longrightarrow
\langle f,g\rangle.
}
\tag{22}
\]

The cure for infinite degree has made the positive geometry locally universal. It no longer distinguishes a prime-power edge from the absence of an edge when both endpoints are kept fixed while the prime alphabet opens.

Equation (22) must not be promoted to strong operator convergence on the full Hilbert space. The normalized adjacency vector attached to a fixed shell can retain norm by spreading over more and more remote shell coordinates even though each fixed coordinate tends to zero. That possible escape of mass is exactly why the statement is formulated as finite-core bilinear convergence.

For the Weil-positivity mandate, however, the fixed-core conclusion is already decisive for the intended repair: the known finite-prime resultant coefficient is not retained as a local matrix element of the limiting positive form.

## 5. Exact degree-power trichotomy

A useful one-parameter audit is

\[
R_i=D_i^{-\alpha}.
\tag{23}
\]

For every fixed shell,

\[
\langle\delta_m,Q_i^{(\alpha)}\delta_m\rangle
=d_i(m)^{1-2\alpha}.
\tag{24}
\]

Since `d_i(m)\to\infty`, there are exactly three regimes.

If `\alpha<1/2`, then

\[
d_i(m)^{1-2\alpha}\to\infty,
\tag{25}
\]

so the renormalization has not produced a finite-energy fixed core.

If `\alpha=1/2`, equation (22) applies and

\[
Q_i^{(1/2)}\to I
\quad\text{in finite-core bilinear matrix elements}.
\tag{26}
\]

If `\alpha>1/2`, then the diagonal coefficients tend to zero and, since each local scale tends to zero, all fixed off-diagonal coefficients also tend to zero. Hence

\[
Q_i^{(\alpha)}\to0
\quad\text{on the fixed finite core}.
\tag{27}
\]

Thus the critical exponent `1/2` is not a hidden arithmetic success. It is the unique local degree scaling that keeps unit-order fixed-shell energy, and its limit is the universal identity form. Under-normalize and the original domain divergence remains; over-normalize and the geometry vanishes.

## 6. Matched controls

The obstruction is specifically tied to opening infinitely many prime directions.

Restrict the shell graph to the multiplicative monoid generated by a **fixed finite prime alphabet**. `WP-148` shows that for each fixed vertex the outgoing prime-power tails are summable, so

\[
d_i(m)\longrightarrow d_\infty(m)<\infty.
\tag{28}
\]

The implication (12) then fails: a finite-energy local scale need not tend to zero, and normalized arithmetic edges can remain nonzero. Likewise, on one prime-power ray the edge weights form a geometric tail rather than the nonsummable fresh-prime family.

So the loss of the selector is not a generic defect of normalized graph Laplacians. It is caused by the same genuinely global all-prime proliferation identified in `WP-148` and amplified by the spectator mechanism of `WP-149`.

Several broader escapes remain outside the theorem. A pair-dependent or nonlocal renormalization is not a vertex-local congruence. A cutoff-dependent identification of the test vectors may deliberately follow mass escaping to infinity. A source-forced mixed-prime interaction can alter `J` before normalization. An infinite-dimensional or nonseparable finite--archimedean coupling can change the form before the all-prime limit. None of those constructions inherits a Weil sign theorem from (8) automatically; each would need its own canonicality, selector, archimedean, and positivity audit.

## 7. Relation to the existing obstruction chain

`WP-145`--`WP-147` showed that the zero-order resultant kernel carries the desired finite prime-power support but is not itself conditionally positive and has unbounded two-sided primitive inertia. `WP-148` supplied the canonical finite-cutoff repair: conservative graph-Laplacian positivity, at the price of infinite global degree and a trivial counting-`ell^2` form domain. `WP-149` then eliminated faithful changes of ambient measure and the unchanged resistance-space quotient by showing that the all-prime graph has only constant finite-energy functions.

`WP-150` closes the next canonical response: **change the positive cutoff energy locally instead of changing the ambient measure**. Finite degree-normalized forms do exist and remain PSD, but any local scaling strong enough to make every fixed shell finite-energy necessarily sends all fixed arithmetic edges to zero.

This also sharpens the remaining interpretation of `CLUE-mixed-prime-positive-completion-selector-quotient`. The unresolved route is not a hidden local normalization of the sparse resultant graph. Any surviving positive completion must retain or create genuinely nonlocal/mixed structure, alter the finite observable before the limit, or assemble the archimedean sector nonseparably rather than normalize each divergent shell degree independently.

## 8. Prior art and novelty audit

None of the generic graph theory used here is claimed as new. The symmetric normalized Laplacian

\[
I-D^{-1/2}AD^{-1/2}
\]

is standard; a classical reference is Fan R. K. Chung, *Spectral Graph Theory*, CBMS Regional Conference Series in Mathematics 92, American Mathematical Society, 1997. Infinite weighted graph Laplacians and their Dirichlet forms are likewise classical; see, for example, S. Haeseler, M. Keller, D. Lenz, and R. K. Wojciechowski, *Laplacians on infinite graphs: Dirichlet and Neumann boundary conditions*, Journal of Spectral Theory **2** (2012), 397--432, DOI `10.4171/JST/35`. Apostol's 1970 cyclotomic-resultant theorem supplies the arithmetic support and fresh-prime weights used in `WP-145`--`WP-149`.

Targeted searches for normalized graph-Laplacian or degree-normalization treatments of cyclotomic-resultant graphs did not locate this exact construction. The novelty claim is therefore narrow and Mathia-specific: equations (10)--(17) combine the already-derived Prime-Circle critical resultant degree divergence with arbitrary positive vertex-local congruences and prove that **finite fixed-shell energy forces complete erasure of every fixed arithmetic edge**. Equations (23)--(27) then classify the canonical degree-power family.

This is not a new normalized-Laplacian theorem in graph theory, not a Weil criterion, and not evidence for RH. It is a structural no-go for one natural way of trying to preserve the independent finite-cutoff positivity discovered in `WP-148` after `WP-149` destroyed the unrenormalized global energy space.

## 9. Consequence for the research mandate

The resultant route now exhibits a sharp three-way conflict. Keeping the original off-diagonal arithmetic coefficients gives the canonical positive graph energy but an unusable all-prime global domain (`WP-148`--`WP-149`). Renormalizing locally enough to restore finite fixed-shell energies preserves positivity but destroys those coefficients (`WP-150`). Renormalizing more weakly leaves the divergence.

Hence the route

\[
\boxed{
\text{exact resultant selector}
\to
\text{finite graph positivity}
\to
\text{vertex-local finite-energy renormalization}
\not\to
\text{global Weil-positive selector}
}
\tag{29}
\]

is closed.

A plausible continuation must therefore alter the construction **before** the local degree normalization problem appears: introduce a Mathia-forced cross-prime interaction, a nonlocal quotient/compression with a genuinely new sign theorem, a moving test-space identification justified independently of the target coefficients, or a finite--archimedean geometry whose coupling is already present before the all-prime limit. It must still reproduce the finite prime-power amplitudes and the archimedean/polar terms from the same canonical structure rather than by compensating regularization.

## Internal dependencies

- `research/prime_circle/findings/PC-004-normalized-resultants-weil-local-kernels.md`
- `research/weil_positivity/findings/WP-145-resultant-hessian-positivity-loses-prime-power-support-and-splits-real-place-curvature.md`
- `research/weil_positivity/findings/WP-146-critical-resultant-kernel-is-conditionally-indefinite-on-mixed-prime-three-chain.md`
- `research/weil_positivity/findings/WP-147-disjoint-resultant-chains-force-unbounded-primitive-two-sided-inertia.md`
- `research/weil_positivity/findings/WP-148-canonical-resultant-graph-laplacian-has-infinite-critical-degree-and-trivial-l2-domain.md`
- `research/weil_positivity/findings/WP-149-spectator-prime-parallel-paths-collapse-resultant-resistance-and-energy-space.md`
- `research/weil_positivity/clues/CLUE-mixed-prime-positive-completion-selector-quotient.md`
