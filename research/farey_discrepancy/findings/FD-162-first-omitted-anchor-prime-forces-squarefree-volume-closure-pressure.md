# FD-162 — First omitted anchor primes force squarefree-volume closure pressure

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact obstruction / arbitrary prime-avoidance anchors / terminal divisor-closure pressure
- **Depends on:** FD-159, FD-160, FD-161

## Claim

FD-161 closes terminal auxiliary migration for the initial-prime anchor `S_s={p_1,...,p_s}` by recovering one full Boolean face inside half of a principal divisor closure. That argument is stronger than necessary for the Cheeger inequality: FD-159 prices the **number of occupied primary states**, not the dimension of a complete Boolean subface.

Counting all low squarefree primary states gives a substantially stronger law and removes the exact initial-segment hypothesis. The relevant parameter is the **first prime omitted by the anchor**.

Let `p_1=2<p_2<...` denote the primes. For any finite nonempty prime set `S`, define its initial-prime coverage

\[
m(S):=\max\{m\ge0:\{p_1,\ldots,p_m\}\subseteq S\},
\qquad
\ell_S:=p_{m(S)+1}.
\tag{1}
\]

Thus `ell_S` is the smallest prime not in `S`. Retain from FD-159 the squarefree vertex set `V_T`, the `S`-free anchor set `D_(S,T)`, the anchored Cheeger constant `h_(S,T)`, parent distortion `P_(S,T)`, occupied primary-fiber count `f_(S,T)(d)`, outgoing leakage `L_(S,C,T)`, and optional child distortion `K_(S,T)`. Put

\[
Q_{\rm sf}(x):=\#\{n\le x:\mu^2(n)=1\}.
\tag{2}
\]

Take any nontrivial active auxiliary core

\[
c\in D_{S,T},
\qquad
c>1,
\qquad
p_*c\le T,
\qquad
p_*:=\min S,
\tag{3}
\]

and its principal divisor ideal

\[
D(c):=\{d:d\mid c\}.
\tag{4}
\]

Then

\[
\boxed{
\bar f_{S,D(c)}(T)
\ge
\frac{Q_{\rm sf}(\ell_S-1)-1}{2}.
}
\tag{5}
\]

Consequently FD-159 gives

\[
\boxed{
P_{S,T}
+
\frac{L_{S,D(c),T}}{2^{\omega(c)}}
\ge
\frac{h_{S,T}}2\bigl(Q_{\rm sf}(\ell_S-1)-1\bigr).
}
\tag{6}
\]

If the child distortion satisfies

\[
\eta_T^+(v)\le K_{S,T}\nu_T(v)
\qquad(v\in R_{S,T}),
\tag{7}
\]

then the distinct outer recipients obey

\[
\boxed{
|C_{\rm out}(S,D(c),T)|
\ge
\frac{2^{\omega(c)}}{K_{S,T}}
\left(
\frac{h_{S,T}}2\bigl(Q_{\rm sf}(\ell_S-1)-1\bigr)-P_{S,T}
\right)_+.
}
\tag{8}
\]

The elementary squarefree-counting identity

\[
Q_{\rm sf}(x)
=
\sum_{d\le\sqrt x}\mu(d)\left\lfloor\frac{x}{d^2}\right\rfloor
=
\frac{x}{\zeta(2)}+O(\sqrt x)
\tag{9}
\]

and the prime number theorem imply that, whenever `m=m(S)->infinity`,

\[
\boxed{
\frac{Q_{\rm sf}(\ell_S-1)-1}{2}
=
\left(\frac1{2\zeta(2)}+o(1)\right)m\log m.
}
\tag{10}
\]

Hence any anchor family that eventually contains every fixed prime has **growing terminal divisor-closure pressure of order at least `m log m`**. Under a fixed positive lower bound for `h_(S,T)`, bounded parent distortion, and uniformly bounded normalized principal-closure leakage, no nontrivial active auxiliary core can persist once `m(S)` tends to infinity.

For the initial-prime anchors `S_s={p_1,...,p_s}`, equation (10) strengthens FD-161 from the Boolean-face lower bound

\[
\frac{2^{b_s}-1}{2}=s^{o(1)}
\tag{11}
\]

to

\[
\boxed{
\bar f_{S_s,D(c)}(T)
\ge
\left(\frac1{2\zeta(2)}+o(1)\right)s\log s.
}
\tag{12}
\]

The remaining `different anchor` escape from FD-161 is therefore much narrower than merely choosing a non-initial prime set. With bounded architecture resources and persistent nontrivial auxiliary cores, the initial coverage `m(S)` must stay bounded along an infinite subsequence. Equivalently, after passing to a further subsequence, **one fixed small prime is omitted from every anchor set**. A moving anchor that becomes exhaustive on each fixed prime still pays the same terminal-closure obstruction.

## 1. The first omitted prime makes every smaller squarefree integer a primary state

Choose any prime factor

\[
r\mid c.
\tag{13}
\]

Because `c` is `S`-free, `r` is not in `S`. By definition of the first omitted prime,

\[
\boxed{r\ge\ell_S.}
\tag{14}
\]

Exactly half of the divisors of the squarefree integer `c` omit `r`; these are the divisors

\[
d\mid c/r.
\tag{15}
\]

Now take any squarefree integer `q` satisfying

\[
2\le q<\ell_S.
\tag{16}
\]

Every prime factor of `q` is strictly smaller than `ell_S`. Since `ell_S` is the smallest prime outside `S`, every such prime belongs to `S`. Therefore

\[
q\mid P_S.
\tag{17}
\]

Moreover, for every `d|c/r`,

\[
qd
\le
q\frac cr
<
\ell_S\frac cr
\le
r\frac cr
=c
\le T.
\tag{18}
\]

Thus every squarefree `q` in (16) belongs to the occupied primary fiber `F_(S,T)(d)`. There are exactly

\[
Q_{\rm sf}(\ell_S-1)-1
\tag{19}
\]

such states, the subtraction removing `q=1`. Hence

\[
\boxed{
f_{S,T}(d)
\ge
Q_{\rm sf}(\ell_S-1)-1
\qquad(d\mid c/r).}
\tag{20}
\]

The other half of the principal ideal has nonnegative fiber size. Since `c` is squarefree,

\[
|D(c)|=2^{\omega(c)},
\tag{21}
\]

and averaging (20) over its `2^(omega(c)-1)` guaranteed divisors proves (5).

This uses a larger object than the Boolean subface isolated in FD-161. The recovered states need not form one complete coordinate cube: they are simply **all squarefree primary products below the first omitted prime**. FD-159 only needs their cardinality, so requiring a complete Boolean face discarded most of the available pressure.

## 2. Principal closure is active and FD-159 applies unchanged

Every divisor `d|c` remains squarefree and coprime to `P_S`, so

\[
D(c)\subseteq D_{S,T}.
\tag{22}
\]

The activity hypothesis in (3) is inherited downward:

\[
p_*d\le p_*c\le T
\qquad(d\mid c).
\tag{23}
\]

Thus `D(c)` is an admissible finite divisor down-set for FD-159. Substitution of (5) into its average-fiber leakage law gives (6), and substitution into its child-distortion recipient bound gives (8).

No property of the edge architecture beyond the quantities already isolated in FD-159 is added here. In particular, the proof remains valid for arbitrary multi-parent positive divisibility architectures covered there.

## 3. Exhausting the small primes forces `m log m` closure pressure

For completeness, (9) follows directly from

\[
\mu^2(n)=\sum_{d^2\mid n}\mu(d).
\tag{24}
\]

Summing over `n<=x` gives

\[
Q_{\rm sf}(x)
=
\sum_{d\le\sqrt x}\mu(d)\left\lfloor\frac{x}{d^2}\right\rfloor.
\tag{25}
\]

Replacing the floor by `x/d^2+O(1)` contributes `O(sqrt x)`, while the omitted tail of the absolutely convergent series for `1/zeta(2)` contributes another `O(sqrt x)`. This proves (9) without a new external input.

If `m=m(S)->infinity`, then

\[
\ell_S=p_{m+1}
=(1+o(1))m\log m
\tag{26}
\]

by the prime number theorem, already anchored in `SOURCES.md`. Combining (9) and (26) proves (10).

Suppose now that along such a family

\[
h_{S,T}\ge h_0>0,
\qquad
P_{S,T}\le P_0,
\qquad
\frac{L_{S,D(c),T}}{2^{\omega(c)}}\le L_0
\tag{27}
\]

for fixed constants. Equation (6) would force

\[
P_0+L_0
\ge
\left(\frac{h_0}{2\zeta(2)}+o(1)\right)m\log m,
\tag{28}
\]

a contradiction. Thus persistent nontrivial auxiliary cores require at least one of anchored expansion, parent distortion, or normalized outer leakage to deteriorate unless the first missing prime remains bounded.

The subsequence formulation is exact. If `m(S)` does not tend to infinity, there is an infinite subsequence on which `m(S)<=M` for some fixed `M`. The first omitted prime then belongs to the finite set `{p_1,...,p_(M+1)}`, so one fixed prime is omitted on a further infinite subsequence. This is the structural form of the surviving alternative-anchor escape.

## 4. Stress tests and sharp boundaries

The theorem intentionally becomes silent when a small prime hole is persistent. If `2 notin S`, then `ell_S=2` and `Q_sf(ell_S-1)-1=0`. This is not a defect of the proof: an `S`-free auxiliary core may then use the prime `2`, and there is no universal reservoir of nontrivial primary products below it. More generally, bounded `m(S)` gives only a bounded first-gap reservoir. The result therefore does **not** rule out anchor geometries that permanently omit one or more low primes.

The theorem also excludes `c=1`. The root has no auxiliary prime factor with which to expose half of a principal divisor cube. Its primary fiber is controlled directly by FD-159 and does not represent terminal migration.

The squarefree-volume lower bound is deliberately one-sided. There can be many additional primary products above `ell_S`, and several auxiliary prime factors can expose larger portions of the closure. Equation (5) is only the universal contribution forced by the first omitted prime; no optimality claim is made for the constant `1/2` or for the total fiber size.

As in FD-159--FD-161, equations (5)--(8) are architecture statements. They do not prevent `h_(S,T)` from decaying, `P_(S,T)` or `K_(S,T)` from growing, or a construction from deliberately paying large outer leakage. They also do not turn recipient cardinality into independent source information, do not show that Farey discrepancy supplies the required Möbius orientations, and do not connect the resulting coefficient coercivity to the RH-critical Franel--Landau destination. The information-budget gate remains downstream.

## 5. Prior art, representation audit, and consequence for the line

The ingredients are classical and elementary: divisors of a squarefree integer form a Boolean lattice, all primes below the first omitted prime belong to the anchor set, squarefree integers have density `1/zeta(2)`, and the prime number theorem gives `p_m~m log m`. A targeted prior-art search over squarefree divisor lattices, principal ideals, prime-avoidance sets, Cheeger expansion, and Farey/Möbius discrepancy found only the generic lattice facts and unrelated prime-avoidance terminology, not the first-omitted-prime average-fiber consequence (5)--(6). No novelty is claimed for any of the classical ingredients. No new external theorem is load-bearing, so `SOURCES.md` requires no change.

The representation audit is exact. Neither Farey values nor Möbius signs enter the proof. The only new observation is combinatorial: **the first missing anchor prime converts half of every nontrivial principal auxiliary closure into a reservoir containing every lower squarefree primary product**. This is therefore a stronger architecture obstruction, not a source-specific cancellation theorem.

For the current line, the practical change is quantitative and structural. FD-161 showed that initial-prime anchors recover a diverging Boolean depth after closure. FD-162 shows that the same closure actually contains `Theta(s log s)` guaranteed primary states on average, and that this phenomenon persists for every anchor family whose first omitted prime tends to infinity. Merely perturbing the initial-prime set at moving high primes does not reopen terminal migration. A genuine alternative-anchor escape must retain a low-prime hole, or else pay through expansion, endpoint distortion, or outer leakage.

### Retrieval notes

- Internal inputs: FD-159, FD-160, FD-161, the current `farey_discrepancy` synthesis, current local clue dispositions, and the existing prime-number-theorem anchor in `SOURCES.md`.
- No open local adversarial-review sidecar had owner precedence when this investigation began.
- The squarefree-volume inequality (5) was derived before the external prior-art search; the search was used only to audit novelty and neighboring language.
- `SOURCES.md`, clues, and `mind/**` are unchanged because no new load-bearing source or clue-state transition is introduced.
- No computational or formalization handoff is needed: the decisive step is an exact principal-closure counting argument.