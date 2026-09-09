# NB-008 — finite Nyman residuals have an explicit lcm-scale tail-average witness

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + RESIDUAL-SPECIFIC-LOCALIZATION + LCM-SCALE-CERTIFICATE + EXPONENTIAL-SCALE-BOUNDARY`. `NB-007` proves that every fixed non-target vector has logarithmically divergent full harmonic semigroup defect, but its coefficient `Gamma(h)` does not locate a useful finite witness. The proposed residual-localization clue asks whether the actual finite-section residuals admit a prescribed index budget `B_N` and a quantitative lower bound for the truncated tail-average gauge.

The canonical real-space Báez--Duarte generators make one such bound completely explicit. Let

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\}\subset\mathcal M,
\qquad
r_N=e-P_{V_N}e,
\qquad
d_N=\|r_N\|,
\]

and put

\[
P_N=\operatorname{lcm}(2,3,\ldots,N),
\qquad B_N=P_N+1.
\tag{1}
\]

For

\[
c_n(h)=n\int_0^{1/n}h(x)\,dx,
\qquad
\Gamma_B(r_N)=
\max_{1\le n\le B}\frac{|c_n(r_N)-d_N^2|^2}{n},
\tag{2}
\]

one has the unconditional finite localization

\[
\boxed{
\Gamma_{B_N}(r_N)
\ge
\frac{d_N^2(1-d_N^2)}{4B_N^3}.
}
\tag{3}
\]

The best-residual structure gives a second estimate. Every generator vanishes on the harmonic shell indexed by `P_N`, so `r_N=1` there. Consequently

\[
\boxed{
\Gamma_{B_N}(r_N)
\ge
\frac{(1-d_N^2)^2}{4B_N^3}.
}
\tag{4}
\]

Combining (3)--(4),

\[
\boxed{
\Gamma_{B_N}(r_N)
\ge
\frac{1-d_N^2}{8B_N^3}.
}
\tag{5}
\]

Thus the clue's requested amplitude-and-location theorem is true without numerical conditioning or a finite matrix computation. The price is severe: `P_N` is the least common multiple of all generator periods, so `log P_N=psi(N)=N+o(N)` by the prime number theorem. The guaranteed witness therefore sits at an exponential index and the coefficient in (3) is exponentially small. This closes the bare localization question but not the useful quantitative Nyman problem. Any RH-relevant continuation must beat the lcm scale by exploiting the projection normal equations or finer source structure, rather than periodicity alone.

## 1. Bagchi's generators are periodic on the harmonic intervals

Let

\[
I_n=\left(\frac1{n+1},\frac1n\right],
\qquad e(x)=1.
\]

Bagchi's canonical generators are

\[
g_l(x)=\left\{\frac1{lx}\right\}
-\frac1l\left\{\frac1x\right\}.
\tag{6}
\]

For `x in I_n`, Bagchi records the exact simplification

\[
\boxed{g_l(x)=\left\{\frac nl\right\}.}
\tag{7}
\]

Hence the interval-value sequence of `g_l` has period `l`. Every vector in

\[
F_N:=\operatorname{span}(e,V_N)
\tag{8}
\]

therefore has a `P_N`-periodic interval-value sequence.

Moreover, whenever `n` is a multiple of `P_N`, every `2<=l<=N` divides `n`, so

\[
\boxed{g_l|_{I_n}=0\qquad(2\le l\le N).}
\tag{9}
\]

This gives an immediate finite approximation floor. Since `r_N=e-v_N` for `v_N=P_{V_N}e`,

\[
r_N|_{I_{mP_N}}=1
\qquad(m\ge1).
\tag{10}
\]

In particular

\[
\boxed{
d_N^2\ge\frac1{P_N(P_N+1)}.}
\tag{11}
\]

The stronger sum over all common-zero shells is also valid, but (11) is enough to display the scale. It is far weaker than the known zero-sensitive logarithmic lower-bound regime and is recorded only as a consistency control.

The inequalities `0<d_N<1` are automatic for `N>=2`: (9) rules out `e in V_N`, while `g_2` has nonzero target pairing, so the projection is nonzero.

## 2. Periodicity makes the finite observation map coercive at lcm depth

The reconstruction identity from `NB-004` is

\[
h_n=(n+1)c_n(h)-nc_{n+1}(h),
\tag{12}
\]

where `h_n` is the value of `h` on `I_n`.

Take any unit vector

\[
h\in F_N\cap e^\perp.
\tag{13}
\]

Its interval values are `P_N`-periodic. Since the harmonic intervals partition `(0,1]`,

\[
1=\|h\|^2
=\sum_{n\ge1}\frac{|h_n|^2}{n(n+1)}
\le\max_{1\le j\le P_N}|h_j|^2.
\tag{14}
\]

Choose `j<=P_N` with `|h_j|>=1`, and set

\[
G=\max_{1\le n\le P_N+1}\frac{|c_n(h)|^2}{n}.
\tag{15}
\]

Because `h perpendicular e`, `c_1(h)=0`, although that fact is not needed in the next estimate. From (12),

\[
\begin{aligned}
1
&\le |h_j|\\
&\le (j+1)|c_j(h)|+j|c_{j+1}(h)|\\
&\le\left((j+1)\sqrt j+j\sqrt{j+1}\right)\sqrt G\\
&\le2(P_N+1)^{3/2}\sqrt G.
\end{aligned}
\tag{16}
\]

Therefore

\[
\boxed{
\max_{1\le n\le B_N}\frac{|c_n(h)|^2}{n}
\ge\frac1{4B_N^3}
\qquad
(h\in F_N\cap e^\perp,\ \|h\|=1).
}
\tag{17}
\]

This is a uniform lower singular-value-type statement for the complete tail-average observation family through `B_N`, proved without forming its matrix. It applies to the whole target-augmented finite space, so no residual-specific normal equation has yet been used.

## 3. The actual best residual converts the periodic bound into the clue's inequality

Orthogonal projection gives

\[
\langle r_N,e\rangle=\|r_N\|^2=d_N^2.
\tag{18}
\]

Put

\[
q_N=1-d_N^2=\|P_{V_N}e\|^2
\]

and normalize the target-orthogonal part of the residual by

\[
z_N=
\frac{r_N-d_N^2e}{d_N\sqrt{q_N}}.
\tag{19}
\]

Then `z_N in F_N cap e^perp` and `||z_N||=1`. Since `c_n(e)=1`,

\[
c_n(r_N)-d_N^2
=d_N\sqrt{q_N}\,c_n(z_N).
\tag{20}
\]

Applying (17) to `z_N` proves

\[
\Gamma_{B_N}(r_N)
\ge
\frac{d_N^2q_N}{4B_N^3},
\tag{21}
\]

which is exactly (3), with the clue's prescribed choice

\[
\boxed{
B_N=P_N+1,
\qquad
\kappa_N=\frac1{4(P_N+1)^3}.
}
\tag{22}
\]

Both quantities are specified independently of where the witness happens to occur.

## 4. The common-zero shell gives a stronger residual-specific witness when the error is small

Equation (10) uses information absent from a generic vector of `F_N cap e^perp`. Apply the reconstruction identity (12) to `r_N` at `n=P_N`:

\[
(P_N+1)c_{P_N}(r_N)
-P_Nc_{P_N+1}(r_N)=1.
\tag{23}
\]

Set

\[
\delta_n=c_n(r_N)-d_N^2.
\]

Subtracting the constant contribution from (23) gives

\[
\boxed{
(P_N+1)\delta_{P_N}
-P_N\delta_{P_N+1}=q_N.
}
\tag{24}
\]

If `G=Gamma_(B_N)(r_N)`, then

\[
|\delta_{P_N}|\le\sqrt{P_NG},
\qquad
|\delta_{P_N+1}|\le\sqrt{(P_N+1)G}.
\]

The same estimate as in (16) yields

\[
\boxed{
\Gamma_{B_N}(r_N)
\ge\frac{q_N^2}{4B_N^3}.
}
\tag{25}
\]

Taking the better of (21) and (25), and using
`max(d_N^2,q_N)>=1/2`, proves (5).

This distinction matters conceptually. The augmented-space estimate (21) proves the clue exactly as stated. The residual shell identity (25) additionally uses the canonical source representation and remains nontrivial when `d_N` is small; it is not a generic finite-dimensional conditioning fact.

## 5. Splicing the localized witness into the finite harmonic defect

`NB-007` proves that for every `h`, every index `n`, and every `X>=2n`,

\[
\mathcal E_X(h)
\ge
\frac{|c_n(h)-c_1(h)|^2}{4n}
\left(H_{\lfloor X/n\rfloor}-1\right).
\tag{26}
\]

Choose an index attaining `Gamma_(B_N)(r_N)`. For `X>=2B_N`, monotonicity of the harmonic factor gives

\[
\boxed{
\mathcal E_X(r_N)
\ge
\frac{q_N}{32B_N^3}
\left(H_{\lfloor X/B_N\rfloor}-1\right).
}
\tag{27}
\]

Thus the finite-section residual does possess an explicit finite-depth harmonic certificate. But the scale cost is visible rather than hidden.

Classically

\[
\log P_N=\psi(N)=N+o(N),
\tag{28}
\]

so `B_N=exp(N+o(N))` and the coefficient in (27) is `exp(-3N+o(N))` up to the target-capture factor. Merely normalizing by `log X` does not turn this into a competitive approximation theorem. A cutoff that barely reaches `B_N` has almost no harmonic leverage, while taking `X` much larger does not remove the exponentially small coefficient.

Therefore the periodic/lcm mechanism answers **existence and localization** but not the asymptotic question motivating the line. A useful improvement must prove that the actual projection normal equations force a witness at a substantially smaller index, or obtain a different target-aware estimate that does not pass through this periodicity cost.

## 6. Prior art, falsification controls, and research consequence

The load-bearing external input is Bagchi's canonical real-space formulation, already anchored in `research/nyman_beurling/SOURCES.md`. In particular, Bagchi explicitly proves (6)--(7), the membership `g_l in mathcal M`, and the semigroup structure used in `NB-004`--`NB-007`. The reconstruction identity (12) is already canonical in `NB-004`. Equations (14)--(27) are elementary finite consequences of these exact formulas.

A targeted literature search of Nyman--Beurling finite sections, the periodic discrete generators, and least-common-multiple structure did not locate this exact residual tail-average localization as a named theorem. No novelty claim rests on that absence: the common-zero and periodicity mechanisms are immediate once Bagchi's interval formula is written down. The mathematical contribution here is to quantify exactly what that mechanism buys for the live finite semigroup certificate, and equally importantly what scale it costs.

Several boundaries are load-bearing. First, `P_N` is a **sufficient uniform** index budget, not a proof that smaller localization is impossible. The projection equations `r_N perpendicular V_N` could force a much earlier witness; (17) does not test that extra structure. Second, the exponential scale statement uses the ordinary prime number theorem only to interpret the exact lcm quantity and is not needed for (3)--(27). Third, the shell floor (11) is far weaker than known zero-sensitive Nyman lower bounds and is not an improved approximation theorem. Fourth, no upper bound on the finite harmonic defect has been derived that would convert (27) into a new estimate for `d_N`.

The residual-localization clue is therefore resolved in a narrowed sense. The requested finite witness exists with fully explicit `B_N` and `kappa_N`, and the source-specific shell gives a stronger companion inequality. What remains genuinely open is **sub-lcm localization**: whether best-approximation orthogonality, arithmetic coefficient structure, or another target-aware datum forces the relevant tail-average mismatch at polynomial or otherwise asymptotically useful scale. That is a different theorem from mere finite observability and is the next quantitative gate.