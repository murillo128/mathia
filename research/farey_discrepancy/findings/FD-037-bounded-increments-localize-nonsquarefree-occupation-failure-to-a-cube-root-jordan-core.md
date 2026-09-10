# FD-037 — bounded increments localize nonsquarefree occupation failure to a cube-root Jordan core

**Status:** `EXACT-DERIVED + PHYSICAL-SOURCE-REGULARITY + JOINT-NONSQUAREFREE-OCCUPATION + CUBE-ROOT-CORE-REDUCTION + SCHUR-JORDAN-TAIL + LINEAR-PRIME-BREADTH`.

`FD-034` identifies every nonsquarefree Jordan row as exactly transverse to the distinguished Schur equality direction, while `FD-035` shows that the separate prime-square renormalization inequalities do not force a pointwise projective gap. `FD-036` adds a genuinely physical constraint: the quotient-shell function has increments of absolute value at most one, and this already forces the pointwise bound `epsilon_(H,D) >>_D H^(-1/2)`.

The same bounded-increment law controls the **union** of nonsquarefree rows much more directly than the separate square-divisor recurrences suggest. Let

\[
w(r):=\frac{J_2(r)}{r^2},\qquad
\mathcal H(X):=\sum_{s\le X}\frac{\mathbf M(\lfloor X/s\rfloor)}s,
\]

and for fixed `D>=1` put

\[
E_{H,D}:=\sum_{D<r\le H}w(r)\mathcal H(\lfloor H/r\rfloor)^2,
\]

\[
U_{H,D}:=\sum_{\substack{D<r\le H\\\mu(r)=0}}
 w(r)\mathcal H(\lfloor H/r\rfloor)^2.
\]

For a cutoff `R>D`, define the low-row core

\[
S_{H,D}(R):=\sum_{D<r<R}w(r)\mathcal H(\lfloor H/r\rfloor)^2.
\]

Then there is an absolute constant `C` such that, whenever `D<R<=H-3`,

\[
\boxed{
E_{H,D}
\le
S_{H,D}(R)
+(1+6\zeta(2))U_{H,D}
+C\left(\frac{H^2}{R^3}+H\right).
}
\tag{1}
\]

Choosing `R=ceil(H^(1/3))` and using the unconditional `FD-033` fact `E_(H,D)/H -> infinity` gives the sharp qualitative consequence

\[
\boxed{
\frac{U_{H,D}}{E_{H,D}}\longrightarrow0
\quad\Longrightarrow\quad
\frac{S_{H,D}(\lceil H^{1/3}\rceil)}{E_{H,D}}\longrightarrow1
}
\tag{2}
\]

along every unbounded sequence on which the left-hand condition holds.

Thus the proposed joint-row occupation mechanism cannot fail diffusely. **Any failure of a positive nonsquarefree energy fraction must force asymptotically all physical Schur energy into only the first `O(H^(1/3))` Jordan rows**, equivalently into quotient arguments of size at least `H^(2/3)+O(1)`. Conversely, any uniform positive fraction of energy outside that cube-root core gives a fixed positive lower bound for `U/E`, hence a fixed projective linear-prefix gap.

This does not prove such a fixed gap. It reduces the live problem to a source-specific concentration question at the long-quotient end, where ambient nonsquarefree density is irrelevant and where the bounded-increment pairing used below no longer has enough room to make its total error negligible without additional information.

## 1. The exact source is one-Lipschitz

`FD-033` derives

\[
\mathcal H(X)=\sum_{n\le X}c(n),
\qquad
c(n)=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n.
\tag{3}
\]

Since `phi(rad(n))<=rad(n)<=n`,

\[
|c(n)|\le1.
\tag{4}
\]

Therefore for all nonnegative integers `u,v`,

\[
\boxed{
|\mathcal H(u)-\mathcal H(v)|\le |u-v|.
}
\tag{5}
\]

This is the same elementary physical-source rigidity exploited in `FD-036`; no cancellation theorem is used.

The Jordan weights satisfy the uniform bounds

\[
\boxed{
\frac1{\zeta(2)}\le w(r)\le1.
}
\tag{6}
\]

Indeed

\[
w(r)=\prod_{p\mid r}(1-p^{-2}),
\]

and a finite subproduct is at least the Euler product over all primes, `1/zeta(2)`.

## 2. Every sufficiently high squarefree row has a nearby nonsquarefree witness

Fix an integer `r` with

\[
R\le r\le H-3,
\qquad \mu(r)\ne0.
\]

Because `r` is squarefree it is not divisible by `4`. Define

\[
r^*:=4\left\lceil\frac r4\right\rceil.
\tag{7}
\]

Then

\[
1\le r^*-r\le3,
\qquad
r^*\le H,
\qquad
\mu(r^*)=0.
\tag{8}
\]

Write

\[
u:=\left\lfloor\frac Hr\right\rfloor,
\qquad
v:=\left\lfloor\frac H{r^*}\right\rfloor.
\]

The quotient arguments are close:

\[
|u-v|
\le
H\left(\frac1r-\frac1{r^*}\right)+1
\le
\frac{3H}{r^2}+1.
\tag{9}
\]

By (5),

\[
|\mathcal H(u)|
\le
|\mathcal H(v)|+\frac{3H}{r^2}+1,
\]

so

\[
\mathcal H(u)^2
\le
2\mathcal H(v)^2
+2\left(\frac{3H}{r^2}+1\right)^2.
\tag{10}
\]

The map `r -> r^*` has multiplicity at most three: a fixed multiple of four can have preimages only among its three preceding integers. Hence, using (6),

\[
\begin{aligned}
\sum_{\substack{R\le r\le H-3\\\mu(r)\ne0}}
 w(r)\mathcal H(\lfloor H/r\rfloor)^2
&\le
2\sum_{\substack{R\le r\le H-3\\\mu(r)\ne0}}
 \mathcal H(\lfloor H/r^*\rfloor)^2
+O\left(\sum_{r\ge R}\left(\frac{H^2}{r^4}+1\right)\right)\\
&\le
6\zeta(2)U_{H,D}
+O\left(\frac{H^2}{R^3}+H\right).
\end{aligned}
\tag{11}
\]

The at most three terminal squarefree rows `H-2,H-1,H` contribute only `O(1)` because their quotient argument is `1` and `mathcal H(1)=1`; this is absorbed by the displayed error. Equation (11) is the key union estimate: outside the low-row core, every squarefree energy term is controlled by a bounded-multiplicity nearby nonsquarefree term plus a deterministic Lipschitz cost.

## 3. The joint occupation question becomes a cube-root concentration question

Decompose `E_(H,D)` into rows below `R`, nonsquarefree rows at least `R`, and squarefree rows at least `R`. The first contribution is `S_(H,D)(R)`, the second is at most `U_(H,D)`, and the third is bounded by (11). This proves (1).

Now take

\[
R_H:=\lceil H^{1/3}\rceil.
\tag{12}
\]

For fixed `D`, `D<R_H<=H-3` once `H` is large, and

\[
\frac{H^2}{R_H^3}+H=O(H).
\tag{13}
\]

`FD-033` proves unconditionally that

\[
\frac{E_{H,D}}H\longrightarrow\infty.
\tag{14}
\]

Divide (1) by `E_(H,D)`. Equations (13)--(14) give

\[
1
\le
\frac{S_{H,D}(R_H)}{E_{H,D}}
+(1+6\zeta(2))\frac{U_{H,D}}{E_{H,D}}
+o(1).
\tag{15}
\]

Since `0<=S/E<=1`, equation (2) follows immediately.

There is also a useful converse formulation. If for some fixed `delta>0`

\[
S_{H,D}(R_H)\le(1-\delta)E_{H,D}
\tag{16}
\]

for all sufficiently large `H`, then (15) yields

\[
\boxed{
\liminf_{H\to\infty}
\frac{U_{H,D}}{E_{H,D}}
\ge
\frac{\delta}{1+6\zeta(2)}.
}
\tag{17}
\]

More generally, the same implication holds along any subsequence on which (16) holds asymptotically with a fixed positive `delta`.

The row cutoff has a direct quotient-shell interpretation. For `r<R_H`,

\[
\left\lfloor\frac Hr\right\rfloor
\ge H^{2/3}+O(1),
\tag{18}
\]

so the only surviving escape for `U/E -> 0` is concentration of the energy on the long-quotient values of `mathcal H`. The issue is no longer whether nonsquarefree rows are globally dense; it is whether the physical quotient-shell source can put almost all of its Schur energy into this shrinking set of low Jordan indices.

## 4. Relation to the existing pointwise gap

At every nonsquarefree row the distinguished equality direction has Jordan coordinate zero. Consequently the full projective residual satisfies exactly

\[
\rho_{H,D}^2\ge U_{H,D},
\tag{19}
\]

and hence

\[
\varepsilon_{H,D}:=\frac{\rho_{H,D}^2}{E_{H,D}}
\ge\frac{U_{H,D}}{E_{H,D}}.
\tag{20}
\]

A positive answer to the joint-occupation question would therefore give a **constant** projective gap, substantially stronger than the `FD-036` bound `epsilon_(H,D) >>_D H^(-1/2)`. But `FD-036` does not itself prevent the concentration in (2): its adjacent-row argument controls the total projective residual, including squarefree row mismatch, whereas `U` records only the rows where the equality direction vanishes identically.

Equation (1) also explains where the cube-root scale comes from. Pairing a row `r` with a bounded-distance nonsquarefree witness costs `O(H^2/r^4+1)`. Summing from `R` upward costs `O(H^2/R^3+H)`. With only the unconditional information `E/H -> infinity`, taking `R` at order `H^(1/3)` is the first scale that makes this deterministic error `o(E)`. The exponent `1/3` is therefore a boundary of the current argument, not an asserted arithmetic phase transition.

A stronger lower bound for `E`, a sharper source increment estimate on the relevant long quotients, or a direct identity coupling the first `H^(1/3)` Jordan rows could move this boundary. None is assumed here.

## 5. Scope, prior-art, and falsification boundary

The derivation uses only canonical line ingredients: the exact Schur/Jordan representation and vanishing nonsquarefree equality coordinates from `FD-034`, the physical quotient-shell coefficient formula and unconditional superlinear energy from `FD-033`, and the elementary bounded-increment observation already isolated in `FD-036`. No new external theorem is load-bearing, so `SOURCES.md` requires no update.

A targeted prior-art audit around Farey discrepancy, GCD/Jordan-totient matrices, squarefree decomposition, and summatory functions did not supply an external theorem needed for (1)--(2). No claim is made that bounded-distance squarefree/nonsquarefree pairing or cube-root cutoffs are novel in isolation; the durable content is the exact implication for the current physical Schur-tail occupation question.

The finding is falsified if the bounded-multiplicity map in (7)--(11), the Jordan weight bound (6), or the `O(H^2/R^3+H)` accumulation is incorrect in the stated normalization. It must not be cited as proving `U/E` is bounded below, as ruling out concentration in the cube-root core, as improving the Franel--Landau exponent, or as evidence for or against RH. Its exact conclusion is the localization of any vanishing joint nonsquarefree occupation fraction to the low-row/long-quotient core described in (2).
