# NB-114 — high multi-ordinate zero packets have a quadratic classical target barrier

**Status:** `EXACT-DERIVED + CLASSICAL-BURNOL-INPUT + ARBITRARY-MULTI-ORDINATE-PACKET + QUADRATIC-TARGET-RANK-BARRIER + ACTUAL-ZETA-ZERO-SUPPLY + GLOBAL-HIGH-TAIL-BOUND + SHEAR-TARGET-SEPARATION + FRONTIER-REDUCTION`.

`NB-112` eliminates true multiplicity at a single off-critical zero as a way to supply enough confluent rank, and `NB-113` shows that an arbitrary finite packet at one common ordinate is exactly orthogonal after canonical deflation and has vanishing classical Hardy target mass. The remaining zero-state escape is to collect rank from many **distinct ordinates**, where `NB-098`--`NB-099` show that the canonical deflated Gram can have genuine collective shear.

That escape does not survive at the level of the classical Hardy/model-space target projection. For any finite packet of actual right-half zeta zeros whose ordinates all have magnitude at least `G`, the Burnol target mass is at most `d/G^2`, where `d` is the packet cardinality counted with multiplicity. Consequently an order-one classical target mass at height `G` requires quadratic rank `d=Omega(G^2)`. Actual zeta supplies only `O(G log G)` zeros in any fixed-ratio height shell. More strongly, **all** right-half zeros above height `G`, across all ordinates, have total classical target mass

\[
O\!\left(\frac{\log G}{G}\right)\to0.
\]

Thus relative-ordinate shear can make the canonical state Gram arbitrarily ill-conditioned without producing appreciable classical target access. Any surviving multi-zero mechanism must exploit the **finite arithmetic section/window** in a way that is absent from the continuum Burnol model-space projection; merely finding a worse high-zero packet in the canonical half-line geometry cannot close the target problem.

## 1. Every high zero contributes at most inverse-square target mass

Let `F` be any finite multiset of actual nontrivial zeta zeros

\[
\rho_j=\beta_j+i\gamma_j,
\qquad
\frac12<\beta_j<1,
\qquad
|\gamma_j|\ge G>0,
\tag{1}
\]

with multiplicity retained. Let `B_F` denote the corresponding finite half-plane Blaschke product. As in `NB-113`, Burnol's model-space projection formula gives the classical target mass

\[
\tau(F)
:=
\|P_{K_{B_F}}k_1\|^2
=
1-|B_F(1)|^2.
\tag{2}
\]

For each factor,

\[
|b_{\rho_j}(1)|^2
=
\frac{(1-\beta_j)^2+\gamma_j^2}
     {\beta_j^2+\gamma_j^2}
=1-\delta_j,
\tag{3}
\]

where

\[
\delta_j
:=
\frac{2\beta_j-1}
     {\beta_j^2+\gamma_j^2}.
\tag{4}
\]

Since `1/2<beta_j<1`,

\[
0<\delta_j
\le
\frac1{\gamma_j^2}
\le
\frac1{G^2}.
\tag{5}
\]

Therefore

\[
\tau(F)
=
1-\prod_{j=1}^d(1-\delta_j).
\tag{6}
\]

Writing

\[
S_F:=\sum_{j=1}^d\delta_j,
\tag{7}
\]

and using `prod_j(1-delta_j) >= 1-sum_j delta_j` and `1-delta_j <= e^{-delta_j}` gives the two-sided elementary comparison

\[
\boxed{
1-e^{-S_F}
\le
\tau(F)
\le
S_F.
}
\tag{8}
\]

In particular,

\[
\boxed{
\tau(F)
\le
\sum_{j=1}^d\frac1{\gamma_j^2}
\le
\frac d{G^2}.
}
\tag{9}
\]

Whenever `S_F=o(1)`, `(8)` also gives

\[
\tau(F)=S_F+O(S_F^2).
\tag{10}
\]

So, in the high-zero regime, the classical target defects are asymptotically additive. Relative-ordinate geometry can drastically change conditioning, but it cannot amplify the Burnol target mass beyond the sum of the individual inverse-square defects.

A first consequence is the **quadratic target-rank barrier**. If a packet supported above height `G` has

\[
\tau(F)\ge c>0,
\tag{11}
\]

then `(9)` forces

\[
\boxed{
d\ge cG^2.
}
\tag{12}
\]

This is independent of simplicity, same-ordinate multiplicity, spacing, relative ordinate spread and canonical Gram conditioning.

## 2. Actual zeta cannot supply quadratic rank in a fixed-ratio shell

Now restrict to positive ordinates for counting. Let `N(T)` be the standard number of nontrivial zeros with `0<gamma<=T`, counted with multiplicity. For each fixed `A>1`, the Bellotti--Wong explicit Riemann--von Mangoldt bound anchored in `SOURCES.md` implies

\[
N(AG)-N(G^-)
=O_A(G\log G).
\tag{13}
\]

Hence any right-half packet of actual zeros contained in the shell

\[
G\le\gamma\le AG
\tag{14}
\]

has

\[
d=O_A(G\log G).
\tag{15}
\]

Combining `(9)` and `(15)` gives

\[
\boxed{
\tau(F)
=O_A\!\left(\frac{\log G}{G}\right)
\to0.
}
\tag{16}
\]

Thus allowing arbitrarily many distinct ordinates inside a fixed-ratio high shell does not rescue the classical target mass. The available zero rank is short of the `Omega(G^2)` requirement by a factor of order `G/log G`.

This shell statement already closes the most direct continuation of `NB-113`: replacing a crowded common-ordinate packet by all actual zeros in a macroscopic relative-height window still leaves the packet asymptotically target-poor in the Burnol model-space metric.

## 3. The entire high-zero tail has vanishing classical target mass

The fixed-ratio restriction is unnecessary. Let

\[
S_{\rm all}(G)
:=
\sum_{\substack{\zeta(\rho)=0\\\Im\rho\ge G}}
\frac1{(\Im\rho)^2},
\tag{17}
\]

where **all** nontrivial zeros with positive ordinate are counted with multiplicity, including critical-line and left-half zeros. Since the right-half positive zeros form a subset, `(9)` shows that every finite right-half packet above `G` has target mass at most `S_all(G)`.

The tail can be evaluated directly from zero counting. In Stieltjes form, with `N(G^-)` used to handle a possible zero exactly at the endpoint,

\[
S_{\rm all}(G)
=
\int_{[G,\infty)} t^{-2}\,dN(t)
=
-\frac{N(G^-)}{G^2}
+2\int_G^\infty\frac{N(t)}{t^3}\,dt.
\tag{18}
\]

Write

\[
M(t)
:=
\frac{t}{2\pi}
\log\frac{t}{2\pi e}.
\tag{19}
\]

Bellotti--Wong gives

\[
N(t)=M(t)+O(\log t),
\tag{20}
\]

with an explicit stronger error already recorded in `SOURCES.md`. The endpoint error in `(18)` is `O(log G/G^2)`, and

\[
\int_G^\infty\frac{\log t}{t^3}\,dt
=O\!\left(\frac{\log G}{G^2}\right).
\tag{21}
\]

The main term is elementary:

\[
-\frac{M(G)}{G^2}
+2\int_G^\infty\frac{M(t)}{t^3}\,dt
=
\frac{\log(G/(2\pi))+1}{2\pi G}.
\tag{22}
\]

Consequently

\[
\boxed{
S_{\rm all}(G)
=
\frac{\log(G/(2\pi))+1}{2\pi G}
+O\!\left(\frac{\log G}{G^2}\right).
}
\tag{23}
\]

In particular the positive-ordinate right-half Blaschke tail is absolutely controlled. Exhaust it by increasing finite packets `F_n`; then `(8)`--`(9)` imply convergence of the products and

\[
\boxed{
\tau_+(G)
\le
S_{\rm all}(G)
=O\!\left(\frac{\log G}{G}\right)
\to0.
}
\tag{24}
\]

If one symmetry-completes with the conjugate negative-ordinate right-half zeros as Burnol's full divisor does, the same estimate holds with at most twice the envelope in `(23)`. The order remains `O(log G/G)`.

This is stronger than a shell count: even pooling **every** high right-half zero, no matter how many ordinate scales are used, produces order-one classical target mass.

## 4. Collective shear and classical target access are quantitatively decoupled

`NB-099` supplies the matched adversarial control. The transverse three-state packet of `NB-098` can be translated by an arbitrary common ordinate `Gamma` without changing its raw Gram, canonical deflation matrix or transformed Gram. For fixed horizontal/transverse shape and small `epsilon`,

\[
\kappa_2(C_F)
=\Theta(\epsilon^{-4})
\tag{25}
\]

uniformly in `Gamma`.

Translate that packet to `Gamma->infinity` while keeping its three ordinates within `Gamma+O(epsilon)`. Equation `(9)` gives simultaneously

\[
\tau(F)
=O(\Gamma^{-2}).
\tag{26}
\]

One may even send `epsilon->0` as fast as desired while sending `Gamma->infinity`: the canonical shear can diverge arbitrarily rapidly while the classical target mass tends to zero quadratically. Therefore there is no implication of the form

\[
\text{large canonical shear}
\Longrightarrow
\text{large classical Hardy target access}.
\tag{27}
\]

This stress test is important because the surviving multi-ordinate geometry after `NB-113` is real: `NB-098` did not expose a spurious conditioning artifact. What fails is the attempted **target conversion**. High-zero conditioning and high-zero model-space target occupation are distinct currencies.

## 5. Prior-art and novelty boundary

Burnol's projection/product formula is classical and is already a load-bearing source in `SOURCES.md`. No novelty is claimed for `(2)`, for the factor identity `(3)`, or for the fact that the full off-critical Blaschke product converges. Likewise the Riemann--von Mangoldt zero count and the Bellotti--Wong explicit error used in `(13)` and `(20)` are established source results, not Mathia claims.

A targeted prior-art audit again located Burnol's statement that the product of `|1-1/rho|` over right-half zeros, counted with multiplicity, is the norm of the relevant Nyman projection. That is precisely the external boundary: the product formula itself is not new here. The inverse-square tail estimate `(23)` is an elementary partial-summation consequence of standard zero counting and is not presented as a literature-level novelty either.

The durable Mathia contribution is the **frontier reduction obtained by combining those classical inputs with the current canonical multi-zero program**: arbitrary relative-ordinate packets above height `G` need quadratic rank to carry order-one classical target mass; actual zeta supplies only `O(G log G)` rank per fixed-ratio shell; the entire high tail still carries only `O(log G/G)` mass; and `NB-099` shows at the same time that canonical collective shear can remain arbitrarily bad. Hence collective shear cannot be promoted to a target mechanism through the continuum Burnol projection alone.

## 6. Scope, falsification and surviving frontier

The result is deliberately about the **classical Hardy/model-space target projection**. It does not prove that a finite Báez-Duarte/Nyman arithmetic section containing high-zero signatures is target-poor. Finite truncation can break continuum identities, mix height with the arithmetic cutoff, and couple the zero packet to source coordinates not present in `B_F` alone. Those effects are not estimated here.

That distinction is now the decisive frontier. A successful continuation must show that the finite arithmetic window converts multi-ordinate zero geometry into target access at a scale that survives `(24)`, or else prove that such conversion is impossible. In concrete terms, it should compare a finite target quantity such as `b_N^*G_N^+b_N` or a normed dual certificate with the corresponding continuum model-space projection and isolate the defect term created by truncation/source arithmetic.

The finding is falsified only if one of its scoped ingredients fails: the Burnol finite-divisor projection identity, the elementary factor defect `(4)`, or the stated zero-counting asymptotic. Poor finite-section behavior does not falsify it; that behavior is exactly the remaining mechanism to analyze.

## Consequence

`NB-112` closes one-zero multiplicity, `NB-113` closes common-ordinate multi-zero conditioning, and the present result closes **classical continuum target access for arbitrary high multi-ordinate packets**. The remaining zero-state program is no longer to manufacture more rank or worse shear at high ordinate. It is to quantify whether the finite arithmetic Nyman section creates a target-sensitive transfer that the continuum Blaschke/model-space geometry provably loses.