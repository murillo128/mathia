# AF-240 — one-over-n Li damping preserves the RH root-rate class

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `RH-SUFFICIENT-QUOTIENT`, `CANCELLATION-COHERENCE`, `SCALE-DEPENDENT-FILTER`, `TARGET-METRIC`, `NO-NOVELTY-CLAIM`

## Claim

AF-239 leaves open whether a scale-dependent full-orbit damping `t_n -> 1` can recover the critical-line discrimination boundary without reintroducing the cancellation artifact of AF-238. There is an exact positive boundary layer.

Let

\[
Q(w):=\frac{\xi'}{\xi}(1+w)=\sum_{j\ge0}b_jw^j
\]

and, for `0<t<=1`, let

\[
\Lambda_n(t):=\sum_{k=1}^n\binom nk t^k b_{k-1}.
\tag{1}
\]

Let `(t_n)` be any deterministic real sequence with

\[
0<t_n\le1,
\qquad
n(1-t_n)\longrightarrow c\in[0,\infty).
\tag{2}
\]

Then

\[
\boxed{
\mathrm{RH}
\iff
\limsup_{n\to\infty}|\Lambda_n(t_n)|^{1/n}\le1.
}
\tag{3}
\]

More precisely:

1. **Uniform RH side.** If RH holds, there is a constant `C_xi<infinity`, independent of `n` and of `t in [0,1]`, such that

\[
0\le \Lambda_n(t)\le C_\xi(n^2+n).
\tag{4}
\]

Thus the RH-side root-rate bound is safe not merely for `(2)` but for **every** moving schedule `t_n in [0,1]`.

2. **False-RH side in the regular `1/n` layer.** If RH is false and

\[
q:=\max_{\rho}\left|1-\frac1\rho\right|>1,
\tag{5}
\]

where `rho` ranges over nontrivial zeros with multiplicity, then

\[
\boxed{
\limsup_{n\to\infty}|\Lambda_n(t_n)|^{1/n}=q.
}
\tag{6}
\]

By reflection symmetry and the Keiper-Li generating-function radius, this `q` is the ordinary Li root rate from AF-235.

3. **Exact damping scale on a critical-line orbit.** For a fixed zero `rho=1/2+i gamma`, its zero-factor response satisfies

\[
\left|1-\frac{t_n}{\rho}\right|^n
\longrightarrow
\exp\!\left(-\frac{c}{2|\rho|^2}\right).
\tag{7}
\]

Hence `1-t_n=o(1/n)` gives asymptotically no damping, `1-t_n~c/n` gives only a finite nonzero attenuation, and suppressing every fixed critical-line orbit to zero requires the strictly stronger regime `n(1-t_n)->infinity`.

The consequence is sharp for the present question: **moving the fixed AF-239 damping back toward `t=1` at the regular `1/n` scale restores the exact binary RH endpoint, but it does not yet buy asymptotic cancellation suppression or any source-depth compression.**

## Zero-sum representation

Using the symmetrically ordered Hadamard product for `xi`, the local logarithmic derivative gives the generalized Li zero sum

\[
\Lambda_n(t)
=
\sum_\rho
\left[1-\left(1-\frac t\rho\right)^n\right],
\tag{8}
\]

with conjugate zeros paired. This is the reflected-zero form of the local factor used in AF-239: replacing `rho` by `1-rho` turns `1+t/(rho-1)` into `1-t/rho`. The functional equation makes the two indexed zero multisets identical.

For fixed `t`, `(8)` lies in the classical parameterized Li-criterion setting. The issue here is different: after substituting `t=t_n`, the sequence is no longer the Taylor coefficient sequence of one fixed generating function, so the fixed-parameter Cauchy-Hadamard argument from AF-239 does not by itself prove `(3)`.

## Derivation

### Under RH, the whole moving family has a uniform polynomial bound

Assume RH and pair `rho=1/2+i gamma` with its conjugate. Put

\[
r=1-\frac t\rho.
\]

Since `Re(rho)=1/2`,

\[
|r|^2
=1-\frac{t(1-t)}{|\rho|^2}
\le1.
\tag{9}
\]

The conjugate-pair contribution to `(8)` is

\[
A_{n,\rho}(t)=2(1-\Re r^n).
\]

Use the exact identity

\[
2(1-\Re r^n)
=|1-r^n|^2+1-|r|^{2n}.
\tag{10}
\]

Because `|r|<=1`,

\[
|1-r^n|
\le n|1-r|
=\frac{nt}{|\rho|},
\tag{11}
\]

and, with `x=|r|^2 in [0,1]`,

\[
1-|r|^{2n}
=1-x^n
\le n(1-x)
=\frac{nt(1-t)}{|\rho|^2}.
\tag{12}
\]

Therefore

\[
0\le A_{n,\rho}(t)
\le
\frac{n^2t^2+nt(1-t)}{|\rho|^2}
\le
\frac{n^2+n}{|\rho|^2}.
\tag{13}
\]

The classical zero count implies

\[
\sum_{\Im\rho>0}\frac{m_\rho}{|\rho|^2}<\infty.
\tag{14}
\]

Summing `(13)` proves `(4)` and absolute convergence of the paired zero sum under RH. In particular, no aggregate high-zero instability appears when `t` varies with `n`: the entire interval `0<=t<=1` is uniformly safe on the RH side.

### A false-RH exponential mode survives a convergent `1/n` perturbation

Now assume RH is false and define

\[
u_\rho:=1-\frac1\rho.
\]

Because the zero set is invariant under `rho -> 1-rho`, an off-critical zero produces one member with `|u_rho|>1`. Moreover `|u_rho|->1` uniformly as `|Im rho|->infinity`, so the maximum `q` in `(5)` is attained by a finite nonempty set

\[
M:=\{\rho:|u_\rho|=q\}.
\tag{15}
\]

Write `epsilon_n=1-t_n`. For every fixed zero,

\[
1-\frac{t_n}{\rho}
=u_\rho\left(1+\frac{\epsilon_n}{\rho-1}\right).
\tag{16}
\]

Condition `(2)` gives

\[
\left(1+\frac{\epsilon_n}{\rho-1}\right)^n
\longrightarrow
\exp\!\left(\frac{c}{\rho-1}\right),
\tag{17}
\]

so each dominant zero contributes

\[
\left(1-\frac{t_n}{\rho}\right)^n
=
q^n z_\rho^n
\left[
\exp\!\left(\frac{c}{\rho-1}\right)+o(1)
\right],
\qquad
z_\rho:=\frac{u_\rho}{q},\quad |z_\rho|=1.
\tag{18}
\]

The points `z_rho` are distinct because `rho -> 1-1/rho` is injective. The coefficients in brackets tend to nonzero constants. Hence the finite normalized dominant sum cannot be exponentially cancelled for all `n`: for distinct unit-modulus `z_j` and nonzero coefficients `a_j`, the Cesaro mean-square identity

\[
\frac1N\sum_{n=1}^N
\left|\sum_j a_j z_j^n\right|^2
\longrightarrow
\sum_j|a_j|^2
\tag{19}
\]

shows that its limsup magnitude is bounded away from zero.

It remains to show that all other zeros have strictly smaller exponential rate. Choose

\[
1<q_0<q_1<q.
\]

Only finitely many zeros satisfy `|u_rho|>q_0`; include them in a finite set `F` containing `M`. Since `epsilon_n=O(1/n)` and nontrivial zeros stay a positive distance from `0`, for all sufficiently large `n` every zero outside `F` satisfies

\[
\left|1-\frac{t_n}{\rho}\right|\le q_1.
\tag{20}
\]

For the zeros outside `F` with `|Im rho|<=2n`, the classical estimate `N(T)=O(T log T)` and `(20)` give total contribution

\[
O(n\log n\,q_1^n).
\tag{21}
\]

For `|Im rho|>2n`, pair conjugates and put `x=t_n/rho`. Since `n|x|` is uniformly bounded away from the binomial singular regime, expansion of `(1-x)^n` gives

\[
\left|
2\left(1-\Re(1-x)^n\right)
\right|
\ll
\frac{n^2}{|\rho|^2}.
\tag{22}
\]

Partial summation from `N(T)=O(T log T)` yields

\[
\sum_{|\Im\rho|>2n}\frac{m_\rho}{|\rho|^2}
=O\!\left(\frac{\log n}{n}\right),
\tag{23}
\]

so the high-zero tail is only `O(n log n)`. The finite set `F\setminus M` has some exponential rate strictly below `q`. Combining `(18)--(23)` gives

\[
q^{-n}\Lambda_n(t_n)
=-\sum_{\rho\in M}
m_\rho e^{c/(\rho-1)}z_\rho^n+o(1)
\]

up to terms of exponential rate below `q`. Equation `(19)` then proves the lower root-rate bound `q`, while the same decomposition gives the upper bound. This proves `(6)`.

### The `1/n` scale is exactly the finite-attenuation layer

For a fixed critical-line zero `rho=1/2+i gamma`,

\[
\left|1-\frac{t_n}{\rho}\right|^2
=1-\frac{t_n(1-t_n)}{|\rho|^2}.
\tag{24}
\]

Taking logarithms and using `epsilon_n=1-t_n`,

\[
n\log\left|1-\frac{t_n}{\rho}\right|
=-\frac{n t_n\epsilon_n}{2|\rho|^2}
+O(n\epsilon_n^2).
\tag{25}
\]

Under `(2)`, `n epsilon_n^2 ->0`, so `(7)` follows.

This exposes three distinct scales. If `n epsilon_n->0`, the fixed critical orbit is essentially undamped. If `n epsilon_n->c in (0,infinity)`, it receives a constant attenuation but remains order one. If `n epsilon_n->infinity` while `epsilon_n->0`, every fixed critical orbit is driven to zero. The last regime is the first one that could provide asymptotically strong cancellation margin while still returning the fixed-parameter boundary to `1/2`.

## Prior art and novelty assessment

The underlying fixed-parameter family is not new. Pedro Freitas, **“A Li-Type Criterion for Zero-Free Half-Planes of Riemann's Zeta Function,”** *Journal of the London Mathematical Society* 73(2) (2006), 399–414, DOI `10.1112/S0024610706022599`, develops parameterized Li coefficients whose sign/growth behavior characterizes zero-free half-planes. Bombieri and Lagarias, **“Complements to Li's Criterion for the Riemann Hypothesis,”** *Journal of Number Theory* 77(2) (1999), 274–287, provide the general multiset/conformal framework. Keiper's 1992 generating-function formulation and Voros's 2006 asymptotic dichotomy supply the ordinary `t=1` radius and false-RH exponential background used in AF-235.

The zero-counting and symmetric Hadamard-product facts used above are classical; see E. C. Titchmarsh, revised by D. R. Heath-Brown, ***The Theory of the Riemann Zeta-function***, 2nd ed., Clarendon Press, Oxford (1986).

No novelty is claimed for generalized Li coefficients, fixed-parameter zero-free criteria, Hadamard zero sums, or the ordinary false-RH exponential asymptotics. The derived Mathia result is the **moving-parameter placement theorem** `(3)--(7)`: within the AF-239 damping family, a regular `1/n` return to `t=1` preserves the AF-235 binary root-rate discriminator, and the RH-side aggregate is in fact uniformly polynomial for arbitrary schedules in `[0,1]`. This is used as a fidelity boundary, not as a new criterion for RH.

## Exact controls and boundaries

**Fixed damping control.** If `t_n=t<1`, AF-239 applies instead: the root-rate test detects only the wider symmetric strip `t/2<=Re rho<=1-t/2`. Condition `(2)` deliberately excludes that fixed loss of sensitivity.

**Undamped control.** `t_n=1` gives `c=0` and recovers the ordinary Li sequence and AF-235 exactly.

**Critical-line aggregate control.** Equation `(4)` is stronger than a per-zero calculation: under RH it controls the complete infinite zero sum uniformly in `t`. Thus the moving-filter frontier does not need a separate conjectural high-zero estimate on the RH side for this family.

**No strong damping at this scale.** Equation `(7)` shows that finite `c` cannot make even one fixed critical-line orbit vanish asymptotically. The theorem restores RH sensitivity but does not solve AF-238 by creating an asymptotically large cancellation margin.

**No source compression.** Equation `(1)` still consumes all local coefficients `b_0,...,b_{n-1}`. The result changes the filter geometry, not the source-access bill from AF-236.

**Regular-schedule boundary.** The false-RH proof uses convergence of `n(1-t_n)` so that every dominant exponential mode acquires a fixed nonzero coefficient in `(18)`. Merely assuming `t_n->1` does not supply that phase regularity: an `O(1/n)` change in `t_n` creates an order-one phase change in a fixed zero mode. An arbitrary data-dependent or adversarial schedule therefore requires its own no-cancellation theorem. This finding does not claim `(6)` for every sequence `t_n->1`.

**No inference that RH is true.** Equation `(3)` is an equivalence. It does not prove the moving coefficients have subexponential root rate unconditionally.

## Consequences for the research frontier

AF-239's first unresolved requirement — aggregate control of the high critical-line zeros under moving damping — is now closed for the entire interval `0<=t<=1`: under RH the full family is `O(n^2)` uniformly in the moving parameter.

The useful unresolved regime is correspondingly narrower. A damping schedule with `n(1-t_n)->infinity` and `t_n->1` would suppress every fixed critical-line orbit while moving the fixed-parameter discrimination boundary back to `1/2`; however, one still has to prove that an off-critical dominant exponential signal cannot be phase-cancelled by the moving parameter and that the resulting construction buys any genuine reduction in source access. The `1/n` layer proves that endpoint recovery is possible, but also that finite attenuation alone is not the missing compression mechanism.
