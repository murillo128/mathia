# AF-241 — mesoscopic Li damping suppresses fixed critical orbits without losing RH root rate

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `RH-SUFFICIENT-QUOTIENT`, `CANCELLATION-COHERENCE`, `SCALE-DEPENDENT-FILTER`, `TARGET-METRIC`, `NO-NOVELTY-CLAIM`

## Claim

AF-240 proves that the regular boundary layer `1-t_n=O(1/n)` preserves the ordinary Li root-rate discriminator, but at that scale every fixed critical-line zero receives only finite attenuation. There is a strictly larger **mesoscopic damping window** in which both desired properties hold at once: every fixed RH-compatible zero factor is driven to zero, while any off-critical dominant exponential mode still forces the ordinary Li root rate.

Let

\[
Q(w):=\frac{\xi'}{\xi}(1+w)=\sum_{j\ge0}b_jw^j,
\qquad
\Lambda_n(t):=\sum_{k=1}^n\binom nk t^k b_{k-1}.
\tag{1}
\]

Write

\[
\varepsilon_n:=1-t_n,
\qquad
\delta_n:=n\varepsilon_n,
\tag{2}
\]

and assume the deterministic real schedule satisfies

\[
0<t_n\le1,
\qquad
\varepsilon_n\to0,
\qquad
\delta_n\to\infty,
\qquad
n\varepsilon_n^2\to0,
\qquad
\delta_{n+1}-\delta_n\to0.
\tag{3}
\]

Then

\[
\boxed{
\mathrm{RH}
\iff
\limsup_{n\to\infty}|\Lambda_n(t_n)|^{1/n}\le1.
}
\tag{4}
\]

If RH is false and

\[
q:=\max_\rho\left|1-\frac1\rho\right|>1,
\tag{5}
\]

then in fact

\[
\boxed{
\limsup_{n\to\infty}|\Lambda_n(t_n)|^{1/n}=q,
}
\tag{6}
\]

so the moving damping has exactly the same binary root-rate decoder as the ordinary Li sequence.

At the same time, for every fixed critical-line zero `rho=1/2+i gamma`,

\[
\boxed{
\left|1-\frac{t_n}{\rho}\right|^n
=
\exp\!\left(
-\frac{\delta_n}{2|\rho|^2}(1+o(1))
\right)
\longrightarrow0.
}
\tag{7}
\]

Thus the conflict visible in AF-239 and AF-240 is not an absolute one. A filter can return to the RH-sensitive endpoint `t=1` while giving asymptotically strong attenuation to every fixed critical-line orbit, provided the return is slower than `1/n` but still sufficiently regular.

A concrete family is

\[
t_n=1-c n^{-\alpha},
\qquad c>0,
\qquad \frac12<\alpha<1,
\tag{8}
\]

for all sufficiently large `n`. Here `delta_n=c n^{1-alpha}->infinity`, `n epsilon_n^2=c^2 n^{1-2alpha}->0`, and `delta_{n+1}-delta_n->0`.

The damping also has an exact moving **height horizon** on the critical line. If `rho_n=1/2+i gamma_n` is any sequence of critical-line zeros, then

\[
\log\left|1-\frac{t_n}{\rho_n}\right|^n
=
-\frac{\delta_n}{2|\rho_n|^2}
\left(1+o(1)\right),
\tag{9}
\]

uniformly along such sequences. Consequently the oscillatory zero factor is strongly suppressed for `|rho_n|^2=o(delta_n)`, receives order-one attenuation when `|rho_n|^2` is comparable with `delta_n`, and is asymptotically undamped when `|rho_n|^2>>delta_n`. Mesoscopic damping therefore does not erase the whole critical-line population; it pushes the surviving cancellation burden upward to heights of order `sqrt(delta_n)` and above.

## Zero-sum representation and RH-side control

As in AF-239/AF-240, symmetric Hadamard ordering gives

\[
\Lambda_n(t)
=
\sum_\rho
\left[
1-\left(1-\frac t\rho\right)^n
\right],
\tag{10}
\]

with conjugate zeros paired.

Under RH, AF-240 already proves uniformly for every `t in [0,1]` that

\[
0\le \Lambda_n(t)\le C_\xi(n^2+n).
\tag{11}
\]

Therefore the forward implication in `(4)` needs no new moving-parameter estimate: every schedule covered by `(3)` is automatically root-subexponential under RH. In particular, the stronger damping `delta_n->infinity` does not create a new high-zero instability on the RH side.

What changes relative to AF-240 is the false-RH argument. In the regular `1/n` layer, each dominant zero acquires a fixed nonzero coefficient. In the mesoscopic layer, that coefficient itself tends to zero subexponentially, and different dominant zeros can acquire different subexponential amplitudes and phases. The issue is therefore whether this moving attenuation can cancel the entire dominant exponential shell. Condition `(3)` is sufficient to rule that out.

## Dominant off-critical modes survive mesoscopic damping

Assume RH is false. Put

\[
u_\rho:=1-\frac1\rho.
\tag{12}
\]

Reflection symmetry of the zero set implies that some zero has `|u_rho|>1`. Since `|u_rho|->1` as `|Im rho|->infinity`, the maximum `q` in `(5)` is attained by a finite nonempty set

\[
M:=\{\rho:|u_\rho|=q\}.
\tag{13}
\]

For fixed `rho`,

\[
1-\frac{t_n}{\rho}
=
u_\rho
\left(1+\frac{\varepsilon_n}{\rho-1}\right).
\tag{14}
\]

Because `n epsilon_n^2->0`, the logarithm may be expanded uniformly over the finite set `M`:

\[
n\log\left(1+\frac{\varepsilon_n}{\rho-1}\right)
=
\frac{\delta_n}{\rho-1}+o(1).
\tag{15}
\]

Hence, writing

\[
a_\rho:=\frac1{\rho-1},
\qquad
z_\rho:=\frac{\nu_\rho}{q},
\qquad |z_\rho|=1,
\tag{16}
\]

we obtain

\[
\left(1-\frac{t_n}{\rho}\right)^n
=
q^n z_\rho^n
\exp(\delta_n a_\rho)
(1+o(1)).
\tag{17}
\]

Every member of `M` lies on the left side of the critical line, because `|1-1/rho|>1` is equivalent to `Re rho<1/2`. Therefore

\[
\Re a_\rho
=
\frac{\Re\rho-1}{|\rho-1|^2}<0.
\tag{18}
\]

Let

\[
A:=\max_{\rho\in M}\Re a_\rho<0,
\qquad
M_*:=\{\rho\in M:\Re a_\rho=A\}.
\tag{19}
\]

After dividing the dominant shell by `q^n e^{A delta_n}`, every zero in `M\setminus M_*` vanishes because `delta_n->infinity`. The surviving finite sum is

\[
S_n
:=
\sum_{\rho\in M_*}
m_\rho z_\rho^n
\exp\!\bigl(i\,\Im(a_\rho)\delta_n\bigr),
\tag{20}
\]

up to `o(1)`, where `m_rho` is the zero multiplicity.

The key point is that the slowly moving phases cannot annihilate this whole finite shell. The map `rho -> 1-1/rho` is injective, so the `z_rho` in `(20)` are distinct. For two distinct members `rho,sigma`, set

\[
w=z_\rho\overline{z_\sigma}\ne1,
\qquad
c_n=
\exp\!\left(i[\Im a_\rho-\Im a_\sigma]\delta_n\right).
\tag{21}
\]

The regularity condition `delta_{n+1}-delta_n->0` gives

\[
|c_{n+1}-c_n|\to0.
\tag{22}
\]

Since the partial sums of `w^n` are uniformly bounded, summation by parts yields

\[
\frac1N\sum_{n\le N} w^n c_n\longrightarrow0.
\tag{23}
\]

Indeed the numerator is bounded by a constant times `1+sum_{n<N}|c_{n+1}-c_n|=o(N)`. Expanding the square of `(20)` and applying `(23)` to every off-diagonal pair gives the Cesaro mean-square limit

\[
\frac1N\sum_{n\le N}|S_n|^2
\longrightarrow
\sum_{\rho\in M_*}m_\rho^2>0.
\tag{24}
\]

Thus `limsup |S_n|` is bounded away from zero. The moving damping may attenuate the entire dominant shell by the common subexponential factor `e^{A delta_n}`, but it cannot make that shell exponentially invisible.

## All nondominant zeros remain below the same root rate

The remainder estimate from AF-240 survives because only `epsilon_n->0` is needed for exponential separation away from the finite dominant set.

Choose

\[
1<q_0<q_1<q.
\tag{25}
\]

Only finitely many zeros have `|u_rho|>q_0`; include them in a finite set `F` containing `M`. Since `epsilon_n->0` and nontrivial zeros stay a positive distance from the origin, all sufficiently large `n` satisfy

\[
\left|1-\frac{t_n}{\rho}\right|\le q_1
\tag{26}
\]

for every `rho notin F` with `|Im rho|<=2n`. The classical count `N(T)=O(T log T)` then bounds that finite-height remainder by

\[
O(n\log n\,q_1^n).
\tag{27}
\]

For `|Im rho|>2n`, conjugate pairing and the same large-zero expansion as AF-240 give

\[
\left|
2\left(1-\Re\left(1-\frac{t_n}{\rho}\right)^n\right)
\right|
\ll
\frac{n^2}{|\rho|^2},
\tag{28}
\]

and partial summation from the zero count yields a total `O(n log n)` tail. Every member of the finite set `F\setminus M` has ordinary exponential rate strictly below `q`, because its extra damping factor has `n`th root tending to one.

Finally,

\[
\left(e^{A\delta_n}\right)^{1/n}
=e^{A\varepsilon_n}\longrightarrow1.
\tag{29}
\]

Therefore `(24)`, `(27)--(29)` prove the lower and upper root-rate bounds in `(6)`. This establishes the reverse implication in `(4)`.

## Exact critical-line damping horizon

For `rho=1/2+i gamma`, the zero-factor modulus satisfies the exact identity

\[
\left|1-\frac{t_n}{\rho}\right|^2
=
1-\frac{t_n\varepsilon_n}{|\rho|^2}.
\tag{30}
\]

Hence

\[
\begin{aligned}
n\log\left|1-\frac{t_n}{\rho}\right|
&=\frac n2
\log\left(1-\frac{t_n\varepsilon_n}{|\rho|^2}\right)\\
&=-\frac{\delta_n}{2|\rho|^2}
\left(1+o(1)\right).
\end{aligned}
\tag{31}
\]

For a moving critical-line zero `rho_n`, the same estimate is uniform because nontrivial zeta zeros have `|rho|` bounded away from zero and `epsilon_n->0`. Equation `(9)` follows.

This gives a geometric interpretation of the mesoscopic layer. The moving filter has a zero-height cutoff at

\[
|\gamma|\asymp\sqrt{\delta_n}.
\tag{32}
\]

Below that scale the oscillatory factor is increasingly suppressed; near that scale it retains a nontrivial constant fraction; far above it the factor is nearly unimodular. For the power schedule `(8)`, the damping horizon is

\[
|\gamma|\asymp n^{(1-\alpha)/2}.
\tag{33}
\]

Thus strong fixed-orbit damping is compatible with RH fidelity precisely because the operation does not uniformly contract the whole zero set. The unresolved cancellation is displaced to an increasing-height boundary layer rather than eliminated.

## Prior art and novelty assessment

The underlying Li and generalized-Li machinery is classical. Jerry B. Keiper, **“Power Series Expansions of Riemann's xi Function,”** *Mathematics of Computation* 58(198), 765–773 (1992), supplies the generating-function/root-radius viewpoint. Enrico Bombieri and Jeffrey C. Lagarias, **“Complements to Li's Criterion for the Riemann Hypothesis,”** *Journal of Number Theory* 77(2), 274–287 (1999), give the general multiset/conformal framework. Pedro Freitas, **“A Li-Type Criterion for Zero-Free Half-Planes of Riemann's Zeta Function,”** *Journal of the London Mathematical Society* 73(2), 399–414 (2006), DOI `10.1112/S0024610706022599`, studies fixed-parameter Li-type families that characterize zero-free half-planes. André Voros, **“Sharpenings of Li's Criterion for the Riemann Hypothesis,”** *Mathematical Physics, Analysis and Geometry* 9, 53–63 (2006), gives the ordinary RH/off-RH asymptotic dichotomy used to interpret the root rate. Standard zero-counting and Hadamard-product facts are in Titchmarsh--Heath-Brown, ***The Theory of the Riemann Zeta-function***, 2nd ed. (1986).

The literature audit located fixed-parameter generalized Li criteria and finite-index/zero-free-region variants, but no source in the audited search was used to support a novelty claim for an `n`-dependent damping theorem. **No novelty is claimed here.** The durable result is the exact placement of a regular mesoscopic schedule inside the Arithmetic Fidelity question left by AF-240: it simultaneously gives strong attenuation of each fixed critical-line factor and preserves the ordinary off-RH exponential discriminator.

The proof is deliberately based only on the classical zero representation plus elementary finite exponential-sum orthogonality. If an equivalent moving-parameter theorem exists in the generalized-Li literature, this finding should be reclassified as a direct specialization rather than treated as new mathematics.

## Exact controls and boundaries

**AF-240 boundary.** If `delta_n=n(1-t_n)->c<infinity`, the RH root-rate discriminator is preserved but a fixed critical-line factor approaches a nonzero constant modulus. AF-241 crosses exactly the first scale needed for fixed-orbit suppression by requiring `delta_n->infinity`.

**Fixed damping boundary.** If `t_n=t<1`, AF-239 applies and the binary test loses a fixed strip adjacent to the critical line. AF-241 avoids this because `epsilon_n->0`, so the `n`th-root cost of the moving attenuation tends to one.

**Regularity is real, not cosmetic.** The condition `delta_{n+1}-delta_n->0` is what preserves Cesaro orthogonality after the dominant phases acquire the extra term `Im(a_rho) delta_n`. The theorem does not cover an arbitrary adversarial or zero-dependent schedule `t_n->1`.

**Second-order condition is sufficient, not claimed sharp.** `n epsilon_n^2->0` makes `(15)` a first-order asymptotic with `o(1)` error over the finite dominant shell. The result does not show that the boundary `epsilon_n~n^{-1/2}` is intrinsic. A higher-order phase analysis may enlarge the allowed strong-damping regime.

**No source-depth saving.** As in AF-239 and AF-240, `Lambda_n(t_n)` still consumes the entire local jet `b_0,...,b_{n-1}`. The theorem solves a cancellation-coherence compatibility question, not the AF-236 source-access bill.

**Suppression is pointwise in zero height, not uniform over the critical line.** Equation `(32)` shows why there is no contradiction with the RH-side polynomial aggregate. As `n` grows, the undamped boundary layer moves to larger zero heights. The filter kills every fixed critical orbit while continually admitting new high-zero modes.

**No inference that RH holds.** Equation `(4)` remains an equivalence. Nothing here proves the moving sequence has root rate at most one unconditionally.

## Consequences for the research frontier

The cancellation question left by AF-240 now has a positive answer in a nonempty explicit regime: `1/n << 1-t_n << 1/sqrt(n)` with a slowly varying accumulated damping phase is enough to suppress each fixed critical-line orbit while retaining the exact ordinary Li root-rate discriminator. The simple family `1-t_n=c n^{-alpha}`, `1/2<alpha<1`, witnesses this regime.

This removes **fixed-orbit cancellation coherence** as the immediate obstruction. The remaining bill is more structural. The damping leaves the full `n`-deep local jet in place and merely moves the surviving critical-line activity to the height scale `sqrt(n(1-t_n))`. A useful next theorem must therefore address at least one of two genuinely different questions:

1. whether the second-order restriction can be relaxed to classify the maximal regular moving-damping regime that still preserves the off-RH root rate; or
2. whether the moving height horizon can be realized from a source-side representation whose information/access cost is materially smaller than the full Li jet while preserving the same cancellation before the root-rate quotient.

The first is a filter-classification problem. The second is the actual compression problem. AF-241 shows that they should no longer be conflated.