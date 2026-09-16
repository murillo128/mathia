# FD-161 — Terminal auxiliary cores force growing primorial closure pressure

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact obstruction / terminal auxiliary migration / initial-prime closure pressure
- **Depends on:** FD-155, FD-159, FD-160

## Claim

FD-160 leaves one geometric escape after sparse holes are closed: an auxiliary core can migrate toward the truncation ceiling so that only `O(1)` primary prime coordinates fit above the core itself. For the initial-prime avoidance faces that are asymptotically optimal for thinning anchor mass in FD-155, that escape does **not** survive divisor closure.

Let

\[
S_s:=\{p_1,\ldots,p_s\},
\qquad
P_j:=\prod_{i=1}^j p_i,
\tag{1}
\]

where `p_1=2<p_2<...` are the primes. Define the finite **primorial recovery depth**

\[
b_s
:=
\max\{0\le j\le s:P_j\le p_{s+1}\}.
\tag{2}
\]

Retain from FD-159/FD-160 the squarefree vertex set, uniform vertex law, anchored Cheeger constant `h_(S_s,T)`, parent distortion `P_(S_s,T)`, occupied primary-fiber count `f_(S_s,T)(d)`, outgoing leakage `L_(S_s,C,T)`, and optional child distortion `K_(S_s,T)`.

Take any **nontrivial active auxiliary core**

\[
c\in D_{S_s,T},
\qquad
c>1,
\qquad
2c\le T,
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
\bar f_{S_s,D(c)}(T)
\ge
\frac{2^{b_s}-1}{2}.
}
\tag{5}
\]

Consequently FD-159 gives the exact architecture obstruction

\[
\boxed{
P_{S_s,T}
+
\frac{L_{S_s,D(c),T}}{2^{\omega(c)}}
\ge
\frac{h_{S_s,T}}{2}\,(2^{b_s}-1).
}
\tag{6}
\]

If the child distortion satisfies

\[
\eta_T^+(m)\le K_{S_s,T}\nu_T(m)
\qquad(m\in R_{S_s,T}),
\tag{7}
\]

then the distinct outer recipients of the closed packet obey

\[
\boxed{
|C_{\rm out}(S_s,D(c),T)|
\ge
\frac{2^{\omega(c)}}{K_{S_s,T}}
\left(
\frac{h_{S_s,T}}2(2^{b_s}-1)-P_{S_s,T}
\right)_+.
}
\tag{8}
\]

The prime number theorem implies

\[
\boxed{
 b_s=(1+o(1))\frac{\log s}{\log\log s},
}
\tag{9}
\]

and therefore

\[
\boxed{
2^{b_s}
=
\exp\!\left(
(\log2+o(1))\frac{\log s}{\log\log s}
\right)
\longrightarrow\infty.
}
\tag{10}
\]

Thus a terminal core may have bounded primary depth `r_T(c)`, but **half of its divisor closure automatically regains a diverging primary Boolean face**. For the initial-prime anchors, terminal migration merely hides primary depth at the top element; it cannot hide it from the global cut used by the anchored Cheeger constant.

In particular, along any family with `s->infinity`, `h_(S_s,T)>=h_0>0`, bounded parent distortion, and uniformly bounded normalized leakage on principal closures, no nontrivial active auxiliary core can occur for all sufficiently large `s`. At least one of anchored expansion, parent distortion, or normalized outer leakage must deteriorate at the rate forced by (6).

For the optimal thinning scale `s=s_alpha` of FD-155, where

\[
s_\alpha=\exp\!\bigl(\alpha^{-1+o(1)}\bigr),
\tag{11}
\]

we have

\[
\log(2^{b_{s_\alpha}})
=
\alpha^{-1+o(1)}.
\tag{12}
\]

Hence replacing the direct FD-154 frame by an arbitrary bounded-distortion multi-parent architecture cannot make the terminal-core escape bounded: at anchor exposure `alpha`, any nontrivial auxiliary core still forces a resource bill of coarse scale

\[
\exp\!\bigl(\alpha^{-1+o(1)}\bigr)
\tag{13}
\]

when `h` stays bounded below. This is weaker than the double-exponential direct parent-load cost of FD-155, but it is architecture-level rather than a property of that specific direct frame.

## 1. Omitting one auxiliary prime exposes a full primorial primary face

Because `c>1` is squarefree, choose any prime divisor

\[
\ell\mid c.
\tag{14}
\]

The core is `S_s`-free. Since `S_s` contains **every** prime below `p_(s+1)`, necessarily

\[
\boxed{\ell\ge p_{s+1}.}
\tag{15}
\]

Exactly half of the `2^{omega(c)}` divisors of `c` omit `ell`; these are precisely the divisors of `c/ell`. Let

\[
d\mid c/\ell.
\tag{16}
\]

For every divisor `q` of `P_(b_s)`, definition (2) gives

\[
q\le P_{b_s}\le p_{s+1}\le\ell.
\tag{17}
\]

Since `d<=c/ell`,

\[
qd
\le
\ell\frac c\ell
=c
\le T.
\tag{18}
\]

Every nontrivial divisor `q|P_(b_s)` therefore belongs to the occupied primary fiber `F_(S_s,T)(d)`. There are exactly `2^{b_s}-1` such divisors, so

\[
\boxed{
f_{S_s,T}(d)\ge2^{b_s}-1
\qquad(d\mid c/\ell).}
\tag{19}
\]

The other half of the principal ideal has nonnegative fiber size. Averaging over all divisors of `c` proves (5):

\[
\bar f_{S_s,D(c)}(T)
=
\frac1{2^{\omega(c)}}
\sum_{d\mid c}f_{S_s,T}(d)
\ge
\frac{2^{\omega(c)-1}(2^{b_s}-1)}{2^{\omega(c)}}.
\tag{20}
\]

This argument is independent of how close `c` is to `T`. The core itself may sit at height `T/2` and support only one or a few primary primes. Removing one auxiliary prime factor moves halfway down its Boolean divisor cube and creates enough multiplicative headroom to fit every primary subset drawn from the first `b_s` coordinates.

## 2. The principal closure is an admissible FD-159 packet

Every divisor of `c` remains squarefree and coprime to `P_(S_s)`, so

\[
D(c)\subseteq D_{S_s,T}.
\tag{21}
\]

Moreover (3) gives, for every `d|c`,

\[
2d\le2c\le T.
\tag{22}
\]

Thus `D(c)` is an active divisor-downward core family and all hypotheses of FD-159 apply. Since

\[
|D(c)|=2^{\omega(c)},
\tag{23}
\]

FD-159 equation (11) combined with (5) yields (6) immediately. Its child-distortion recipient bound, FD-159 equation (14), gives (8).

This sharpens the use of principal closure in FD-160. There the closure inherited only the **minimum** depth `r_T(c)` of the top core, leading to

\[
P+L/|D(c)|\ge h(2^{r_T(c)}-1).
\tag{24}
\]

For terminal migration `r_T(c)=O(1)`, so (24) became silent. Equation (5) uses the nonuniform depth profile *inside the same closure*: many lower divisors recover much larger primary fibers even though the top core remains terminal. The escape was therefore an artifact of replacing the closure by its minimum fiber depth, not a genuine low-fiber property of the closed packet.

## 3. Primorial recovery depth diverges at a quantified rate

By the prime number theorem,

\[
\log P_j=\vartheta(p_j)=(1+o(1))p_j
=(1+o(1))j\log j,
\tag{25}
\]

while

\[
\log p_{s+1}=(1+o(1))\log s.
\tag{26}
\]

The threshold `P_j<=p_(s+1)` in (2) is therefore asymptotically

\[
j\log j\le(1+o(1))\log s.
\tag{27}
\]

Inverting `j log j` gives (9). Substitution into `2^{b_s}` gives (10).

The growth is subpower in `s` but faster than every fixed power of `log s`. This is exactly enough for the architectural conclusion: any uniform positive lower bound on `h` is incompatible with simultaneously bounded `P` and bounded principal-closure leakage once nontrivial terminal cores persist and `s` grows.

For the FD-155 thinning family, equation (12) follows by inserting

\[
\log s_\alpha=\alpha^{-1+o(1)}
\tag{28}
\]

into (9). No sharper asymptotic for `s_alpha` is needed for the coarse resource statement (13).

## 4. Stress tests and sharp boundaries

The smallest terminal example already contains the mechanism. If `c=ell` is a single prime outside `S_s`, its principal ideal is `{1,ell}`. The top core `ell` can be arbitrarily close to `T/2` and have tiny primary depth, but the root `1` supports every nonempty divisor of `P_(b_s)` because `P_(b_s)<=ell`. Thus the factor `1/2` in (5) is unavoidable for a universal argument using only one omitted auxiliary prime: exactly one of the two divisors is guaranteed to recover the large face.

The theorem deliberately excludes `c=1`. The root has no auxiliary prime to omit, so it is not a **migrating auxiliary core**. If a construction uses only `c=1`, it has collapsed back to the base primary face; its available depth is governed directly by `T` and the earlier FD-159/FD-160 bounds. Likewise, if no nontrivial `S_s`-free core can fit below `T`, there is no auxiliary terminal-support escape to analyze.

The initial-prime hypothesis is load-bearing. For a general `s`-element prime set `S`, an `S`-free core may contain a small prime omitted from `S`, and (15) fails. FD-155 is what makes the specialization natural rather than cosmetic: among `s` prime coordinates the initial segment `S_s` minimizes the anchor density, so these are precisely the avoidance faces used by the asymptotically cheapest thinning strategy.

Equation (6) is still conditional on the positive-edge anchored architecture. It does not prevent `h_(S_s,T)` from decaying, `P_(S_s,T)` or `K_(S_s,T)` from growing, or the normalized leakage from being intentionally large. It also does not convert recipient cardinality into independent Möbius information, does not show that Farey discrepancy supplies the required coefficient orientation, and does not by itself improve the Franel--Landau exponent.

## 5. Prior art, representation audit, and consequence for the line

The finite combinatorics used above are classical: the divisors of a squarefree integer form a Boolean lattice, exactly half of them omit any chosen prime factor, and primorial growth follows from the prime number theorem. The line already anchors the prime number theorem in `SOURCES.md`, and FD-160 already records lower-shadow/divisor-lattice literature as neighboring language. A targeted search over Boolean-lattice ideals, divisor lattices, primorial growth, Cheeger expansion, and Farey/Möbius discrepancy did not locate the specific average-fiber consequence (5)--(6). No novelty is claimed for Boolean divisor cubes, primorial asymptotics, or Cheeger inequalities themselves, and no new external theorem is load-bearing; `SOURCES.md` therefore requires no change.

The representation audit is exact. No source values, Möbius signs, or Farey data enter the proof. The only new input beyond FD-159 is the initial-prime geometry: every prime in a nontrivial auxiliary core is at least `p_(s+1)`. The conclusion is consequently an **architecture obstruction**, not a source-information theorem.

Within that scope, the main geometric escape left by FD-160 is now closed for the prime-avoidance sequence that matters most for source thinning. A nontrivial core cannot evade growing primary exposure merely by migrating to the ceiling; its lower divisor shadow recovers a primary face of dimension

\[
(1+o(1))\frac{\log s}{\log\log s}.
\tag{29}
\]

The surviving routes are therefore narrower: allow one of the distortion/expansion/leakage resources to deteriorate, abandon the initial-prime avoidance geometry, use only the trivial root core, or introduce a source-native constraint that changes the admissible coefficient flips or connects the coercive coefficient norm to the Franel--Landau destination.

### Retrieval notes

- Internal inputs: FD-155, FD-159, FD-160, the current `farey_discrepancy` synthesis, and current local clue dispositions.
- No open local adversarial-review sidecar had owner precedence when this investigation began.
- The exact finite inequality (5) was derived before the external prior-art search; the search was used only to audit novelty and neighboring language.
- `SOURCES.md`, clues, and `mind/**` are unchanged because no new load-bearing source or clue-state transition is introduced.
- No computational or formalization handoff is needed: the decisive step is an elementary exact divisor-closure argument rather than a bounded machine subproblem or a reusable formal bottleneck.