# WP-227 — Frequency-matched positive completion requires infinite auxiliary trace at the critical Bost–Connes half-density

**Status:** `EXACT-DERIVED + BOST-CONNES-CRITICAL-MODES + OPPOSITE-FREQUENCY-AUXILIARY-SECTOR + POSITIVE-BLOCK-GRAM + TRACE-LOWER-BOUND + CRITICAL-HILBERT-SCHMIDT-FAILURE + MINIMAL-POSITIVE-CONTROL + GLOBAL-ALL-PRIME-DIVERGENCE + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-226` leaves one concrete escape after ruling out self-pairing of the finite Bost--Connes Weil defect: a finite mode of frequency `+k log p` could be paired **before positivity is read off** with a genuinely different source sector carrying the opposite frequency. Unique factorization then makes the zero-frequency pairing rigid: the mode `k log p` can resonate with an opposite source mode only at the same prime power.

That surviving completion has a sharp global cost which can be proved without assuming RH, zero data, a Gamma model, or a target-fitted kernel.

Let

\[
c_{p,k}:=(\log p)p^{-k/2},
\qquad p\ \text{prime},\ k\ge1,
\tag{1}
\]

be the exact critical finite-mode magnitude already source-forced by `WP-216` and retained in the mode decomposition of `WP-226`. After the opposite-frequency identification, consider any finite matched-mode positive Gram completion whose source-mode diagonal block is uniformly bounded by `M I` and whose cross block contains the exact coefficients `c_{p,k}`. Then positivity forces the auxiliary diagonal mass to satisfy

\[
\boxed{
\operatorname{Tr} B_J
\ge
\frac1M\sum_{(p,k)\in J}(\log p)^2p^{-k}
}
\tag{2}
\]

for every finite set `J` of prime-power modes. In the canonical unit normalization `M=1` this is simply `B_J\succeq C_J^*C_J`.

Letting `J` exhaust all prime powers gives

\[
\sum_{p}\sum_{k\ge1}(\log p)^2p^{-k}
=
\boxed{
\sum_p\frac{(\log p)^2}{p-1}
=
+\infty.
}
\tag{3}
\]

Therefore **no positive opposite-frequency completion in this mode-Gram class can carry the exact critical finite Weil amplitudes with a finite-trace auxiliary sector**. The obstruction is genuinely global: every finite prime set has finite cost, but the all-prime completion does not.

The matched control is equally important. Positivity itself does not fail. On the full mode space the diagonal coupling

\[
C=\operatorname{diag}(c_{p,k})
\tag{4}
\]

is bounded and compact, and the minimal block

\[
\boxed{
\begin{pmatrix}
I&C\\
C^*&C^*C
\end{pmatrix}
=
\begin{pmatrix}I\\ C^*\end{pmatrix}
\begin{pmatrix}I&C\end{pmatrix}
\succeq0
}
\tag{5}
\]

exists. What fails at criticality is exactly trace class:

\[
C\notin\mathcal S_2,
\qquad
C^*C\notin\mathcal S_1.
\tag{6}
\]

Thus the route is not killed; it is forced onto a singular/infinite-budget boundary. A surviving finite--archimedean construction must use a non-trace-class auxiliary sector, a continuous/distributional mode realization, a singular weight/trace, or another geometry in which ordinary auxiliary trace is not the relevant finite energy. It must still explain the Gamma and polar terms and obtain the final sign from an independent theorem.

## 1. The exact surviving mode set after `WP-226`

On one prime axis the source-forced defect of `WP-216` is

\[
W_p
=
-(\log p)
\sum_{k\ge1}p^{-k/2}
\left(S_p^k+S_p^{*k}\right).
\tag{7}
\]

Under the Bost--Connes time action,

\[
\tau_t(S_p^k)=e^{ik t\log p}S_p^k,
\qquad
\tau_t(S_p^{*k})=e^{-ik t\log p}S_p^{*k}.
\tag{8}
\]

Hence the nonzero Bohr frequencies are

\[
\omega_{p,k}=k\log p.
\tag{9}
\]

`WP-225` proves that a normal positive map covariant with this source action cannot turn the hollow defect into a nonzero positive operator. `WP-226` then checks the simplest nonlinear escape, self-pairing opposite modes before taking the zero-frequency conditional expectation. That operation is positive but squares the critical coefficient and kills every cross-prime term.

The remaining source-compatible variant is to introduce a **different** sector before zero-mode projection. Suppose it contains a component which can pair with the finite mode `+\omega_{p,k}` at total frequency zero. If another finite mode `-\omega_{q,j}` contributes to the same zero-frequency channel, then

\[
k\log p=j\log q
\tag{10}
\]

and therefore

\[
p^k=q^j.
\tag{11}
\]

Unique factorization gives

\[
\boxed{p=q,\qquad k=j.}
\tag{12}
\]

Thus an exact source-time zero-mode pairing is diagonal in the prime-power frequency labels. Multiplicity inside the auxiliary frequency space is allowed, but different prime-power frequencies cannot trade their required amplitudes with one another.

This is the structural reason that a modewise trace estimate is meaningful here. It is not an arbitrary diagonalization chosen for convenience; it is the resonance decomposition left by the source logarithmic time evolution.

## 2. Finite positive blocks force a quadratic auxiliary cost

Take any finite mode set

\[
J\subset\{(p,k):p\text{ prime},\ k\ge1\}.
\tag{13}
\]

Hilbertize the matched completion after the zero-frequency identification. Let `u_{p,k}` denote the finite-side mode slots and `v_{p,k}` the selected auxiliary slots which carry the opposite raw frequencies. The block Gram on these finite families has the form

\[
\mathcal M_J
=
\begin{pmatrix}
A_J&C_J\\
C_J^*&B_J
\end{pmatrix}
\succeq0.
\tag{14}
\]

The finite source block is assumed only to have a uniform normalization bound

\[
0\preceq A_J\preceq M I
\tag{15}
\]

with one `M<\infty` independent of `J`. The canonical normalized-mode choice is `A_J=I`, so `M=1`.

Exact critical matching requires

\[
\langle u_{p,k},v_{p,k}\rangle_{\mathcal M_J}
=c_{p,k}
=(\log p)p^{-k/2}.
\tag{16}
\]

Phases are irrelevant for the estimate, so only the absolute value is used below.

Write

\[
a_{p,k}:=\langle u_{p,k},A_Ju_{p,k}\rangle,
\qquad
b_{p,k}:=\langle v_{p,k},B_Jv_{p,k}\rangle.
\tag{17}
\]

The `2 x 2` principal Gram minor on the matched pair is positive:

\[
\begin{pmatrix}
a_{p,k}&c_{p,k}\\
\overline{c_{p,k}}&b_{p,k}
\end{pmatrix}
\succeq0.
\tag{18}
\]

Therefore

\[
a_{p,k}b_{p,k}\ge |c_{p,k}|^2.
\tag{19}
\]

Since `a_{p,k}\le M`,

\[
\boxed{
b_{p,k}
\ge
\frac{(\log p)^2p^{-k}}{M}.
}
\tag{20}
\]

Summing the diagonal of the positive auxiliary block gives (2):

\[
\operatorname{Tr}B_J
\ge
\frac1M
\sum_{(p,k)\in J}(\log p)^2p^{-k}.
\tag{21}
\]

No Schur complement, inverse, or infinite-dimensional domain claim is needed for this lower bound. It is already present on every finite truncation, so the all-prime conclusion cannot be evaded by rearranging a conditionally convergent infinite operator expression.

For the unit-normalized case `A_J=I`, standard positive-block factorization sharpens the same statement to the operator inequality

\[
\boxed{B_J-C_J^*C_J\succeq0.}
\tag{22}
\]

Equation (5) shows that equality is attainable. Thus the lower bound is sharp inside the declared block category.

## 3. The critical all-prime trace diverges

For one prime,

\[
\sum_{k\ge1}|c_{p,k}|^2
=(\log p)^2\sum_{k\ge1}p^{-k}
=
\boxed{\frac{(\log p)^2}{p-1}}.
\tag{23}
\]

This is finite for every fixed prime. Consequently neither a one-prime calculation nor any fixed finite set of primes detects the obstruction.

Across all primes,

\[
\sum_p\frac{(\log p)^2}{p-1}
\tag{24}
\]

diverges. For every prime `p\ge3`, `\log p>1`, hence

\[
\frac{(\log p)^2}{p-1}
>
\frac1p,
\tag{25}
\]

and Euler's divergence

\[
\sum_p\frac1p=+\infty
\tag{26}
\]

is sufficient.

Combining (21) with (24), any exhaustion `J_N` of the prime-power modes satisfies

\[
\boxed{
\operatorname{Tr}B_{J_N}\longrightarrow+\infty.
}
\tag{27}
\]

Thus there is no trace-class positive auxiliary Gram block `B` whose finite compressions reproduce all exact critical cross amplitudes while the finite source normalization remains uniformly bounded.

This is precisely a **local-to-global** obstruction. Finite cylinders are harmless; the critical all-prime limit forces the divergence.

## 4. The operator-ideal boundary is exact

Define the diagonal mode coupling on

\[
\ell^2(J_\infty),
\qquad
J_\infty=\{(p,k):p\text{ prime},\ k\ge1\},
\tag{28}
\]

by

\[
Ce_{p,k}=c_{p,k}e_{p,k}.
\tag{29}
\]

The function

\[
f(x)=\frac{\log x}{\sqrt x}
\tag{30}
\]

has maximum `2/e` on `(1,\infty)`, attained at `x=e^2`. Since `k\ge1`,

\[
|c_{p,k}|
\le
\frac{\log p}{\sqrt p}
\le
\frac2e.
\tag{31}
\]

Hence `C` is bounded.

Moreover `c_{p,k}\to0` along the prime-power label set: for fixed `p` the coefficient decays geometrically in `k`, while `\log p/\sqrt p\to0` as `p\to\infty`. Therefore

\[
\boxed{C\text{ is compact}.}
\tag{32}
\]

But its Hilbert--Schmidt norm is exactly the divergent quantity in (3):

\[
\|C\|_{\mathcal S_2}^2
=
\sum_{p,k}|c_{p,k}|^2
=
\sum_p\frac{(\log p)^2}{p-1}
=+\infty.
\tag{33}
\]

Thus

\[
\boxed{C\in\mathcal K\setminus\mathcal S_2.}
\tag{34}
\]

The minimal auxiliary block

\[
B_{\min}=C^*C
\tag{35}
\]

is consequently positive and compact but not trace class:

\[
\boxed{B_{\min}\in\mathcal K_+\setminus\mathcal S_1.}
\tag{36}
\]

This control is important for interpretation. The theorem is **not** a no-go for positive completion. The exact critical amplitudes admit a perfectly ordinary bounded positive block completion. What criticality forbids is finite ordinary trace of the auxiliary block.

It also prevents a false conflation with `WP-218`. There, compactness refers to an **effective correction acting on the original prime-axis Toeplitz state space**, and such corrections cannot move its negative essential spectrum. Here `B_min` is a compact Gram block on the auxiliary **mode-label space**. Its compactness does not establish that eliminating or coupling that sector induces a compact operator on the original prime-axis state space. Any claimed global bridge must still prove that separate step and survive the `WP-218` essential-spectrum test.

## 5. The half-density is exactly the trace-class boundary

The same calculation can be moved away from criticality without changing the construction. Put

\[
c_{p,k}(\sigma)
=(\log p)p^{-k\sigma},
\qquad \sigma>0.
\tag{37}
\]

Then

\[
\sum_{p,k}|c_{p,k}(\sigma)|^2
=
\sum_p
\frac{(\log p)^2}{p^{2\sigma}-1}.
\tag{38}
\]

For every `\sigma>1/2`, comparison with

\[
\sum_{n\ge2}\frac{(\log n)^2}{n^{2\sigma}}
\tag{39}
\]

shows convergence, so the minimal positive auxiliary block is trace class. At

\[
\sigma=\frac12,
\tag{40}
\]

equation (38) becomes exactly (24) and diverges.

Thus the source-selected Bost--Connes critical half-density sits precisely at the endpoint where the natural diagonal opposite-frequency coupling ceases to be Hilbert--Schmidt and its minimal positive companion ceases to be trace class.

This endpoint numerically resembles the earlier `WP-032` Gram threshold, but the operator statement is not the same. In `WP-032` the all-prime critical amplitude was assembled into a **rank-one functional**, and failure of `ell^2` made that form non-closable. Here the diagonal operator `C` is bounded, compact, and fully closable; the positive completion (5) exists. The new obstruction is specifically the impossibility of keeping the **auxiliary positive block trace class** while retaining all exact matched critical amplitudes.

That matched distinction is also an aggressive falsification check against mere repackaging of the old non-closability result.

## 6. Why this does not yet produce the Gamma place

It is tempting to read the forced infinite auxiliary trace as evidence that the missing sector is archimedean. That inference would be unjustified.

The lower bound knows only the exact finite coefficients and the positive-block inequality. It does not derive

- the Gamma-factor digamma kernel;
- the polar terms at `0` and `1`;
- a real-place scaling representation;
- a source-defined renormalized trace;
- a completed Weil test-function domain; or
- a theorem relating the resulting positive form to the global explicit formula.

The minimal completion `B_min=C^*C` is particularly useful as a matched control because it has the required positive sign **without** any of those structures. Its resolved weights are simply

\[
(\log p)^2p^{-k},
\tag{41}
\]

exactly the squared energies already exposed by `WP-226`. Therefore ordinary block positivity cannot be counted as the missing arithmetic sign theorem.

A genuine continuation of this route must derive the infinite/singular auxiliary geometry independently, and then show that its local-to-global decomposition yields the actual archimedean and polar counterterms rather than a generic divergent bath which happens to dominate the finite coefficients.

## 7. Matched controls and prior-art boundary

The finite-dimensional inequality behind (19)--(21) is elementary Gram positivity. In operator language the sharp factorization of positive `2 x 2` block matrices is a standard consequence of Douglas factorization. The classical source is Ronald G. Douglas, **“On majorization, factorization, and range inclusion of operators on Hilbert space,”** *Proceedings of the American Mathematical Society* **17** (1966), 413--415, DOI `10.1090/S0002-9939-1966-0203464-1`.

No novelty is claimed for positive block matrices, Douglas factorization, Schatten ideals, or the fact that `C` is Hilbert--Schmidt exactly when the square of its diagonal is summable.

The Bost--Connes source dynamics is likewise classical: J.-B. Bost and A. Connes, **“Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory,”** *Selecta Mathematica* **1** (1995), 411--457, DOI `10.1007/BF01589495`, supplies the logarithmic time evolution and critical inverse temperature used by `WP-216`.

The explicit-formula coefficient being matched is classical Weil data. In the standard symmetric normalization the prime-power term has magnitude `(log p)p^{-k/2}` before the test-function evaluation, while the archimedean term comes from the Gamma factor. No novelty is claimed for that formula or for Weil's positivity criterion.

Nearby noncommutative-geometric prior art makes the limitation especially important. Alain Connes and Caterina Consani, **“Weil positivity and Trace formula, the archimedean place,”** arXiv `2006.13771` (2020), studies positivity through an infinite-dimensional Hilbert-space compression of the scaling action and phase-space cutoff; Connes's adelic trace-formula program likewise uses a genuinely global noncommutative space. Those constructions are not trace-class auxiliary baths of the mode-Gram form (14), so (27) is not a no-go for Connes/Consani, Sonin, adelic trace, or Hilbert--Polya approaches.

A targeted literature audit found no prior source asserting the specific Mathia reduction proved here: the `WP-216`/`WP-226` source-forced critical Bost--Connes Weil modes, when completed by an exact opposite-frequency positive Gram sector with uniformly bounded finite normalization, force a non-trace-class auxiliary block. The durable delta is this route classification and its sharp minimal control, not any of the classical operator-theory ingredients.

The result is also category-generic in the appropriate way. Replace primes by multiplicatively independent generators `b_j>1` and amplitudes `(log b_j)b_j^{-k/2}`. The same finite block inequality holds. Whether the total auxiliary trace diverges is then controlled by

\[
\sum_j\frac{(\log b_j)^2}{b_j-1}.
\tag{42}
\]

Thus positivity itself is not Riemann-specific. For the actual prime source, the all-prime divergence is forced; for engineered sparse generalized generators it need not be. This is a negative resource theorem, not a hidden characterization of the primes.

## 8. Research disposition

This result passes the substantive-finding gate as a decisive narrowing of the exact survivor left open by `WP-226`.

The sequence of restrictions is now:

\[
\text{source-forced critical Bost--Connes modes}
\xrightarrow{\text{`WP-225`}}
\text{no linear covariant positive orientation}
\xrightarrow{\text{`WP-226`}}
\text{self-pairing squares the half-density}
\xrightarrow{\text{`WP-227`}}
\text{distinct opposite-frequency positive sector requires infinite auxiliary trace}.
\tag{43}
\]

The last arrow is deliberately not a proof that the global route is impossible. It says that a **finite-trace** archimedean or auxiliary Gram completion is impossible in the natural mode-matched category. The exact critical cross coupling remains bounded and even compact, so a non-trace-class positive completion exists and provides the required matched falsifier.

A surviving construction must therefore do at least one of the following: derive a non-trace-class auxiliary positive sector; use continuous/generalized time modes rather than a trace-class discrete mode bath; employ a source-defined singular or renormalized trace; or leave the block-Gram category entirely. In every case it must still produce the Gamma and polar pieces intrinsically and prove the global Weil-type sign independently of RH or inserted zero data.

No RH implication, completed Weil form, archimedean identification, or new general operator theorem is claimed.