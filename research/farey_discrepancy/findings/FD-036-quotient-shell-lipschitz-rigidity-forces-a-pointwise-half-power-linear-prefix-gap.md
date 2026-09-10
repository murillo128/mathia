# FD-036 — quotient-shell Lipschitz rigidity forces a pointwise half-power linear-prefix gap

**Status:** `EXACT-DERIVED + PHYSICAL-SOURCE-REGULARITY + POINTWISE-SCHUR-DEFECT + LINEAR-PRIME-BREADTH + HALF-POWER-GAP + ADJACENT-SQUAREFREE/NONSQUAREFREE-ROWS`.

`FD-031` reduces every fixed positive linear prime-prefix relaxation to a bounded synthetic head and the physical Mertens tail. `FD-032` proves an absolute transverse cost of order `H`, `FD-034` turns square-divisor rows into a positive average projective gap on complete `4`-adic chains, and `FD-035` shows that those scale inequalities plus coarse energy growth do not by themselves rule out isolated horizons with very small normalized defect.

The physical quotient-shell source contains one extra rigidity that the abstract countermodel of `FD-035` deliberately omits: its summatory transform has increments of absolute value at most one. Combining that elementary Lipschitz law with one nearby pair consisting of a squarefree Jordan row and a nonsquarefree Jordan row gives the missing pointwise estimate. For every fixed Schur-head dimension `D>=1`, there are constants `c_D>0` and `H_D` such that

\[
\boxed{
\varepsilon_{H,D}\ge c_D H^{-1/2}
\qquad(H\ge H_D),
}
\tag{1}
\]

where

\[
\varepsilon_{H,D}
:=\frac{\rho_{H,D}^2}{E_{H,D}}
=\sin^2\theta_{H,D}
=\frac{\mathfrak D_{H,D}}{\Delta_{H,D}}.
\tag{2}
\]

Equivalently, the best linear-prefix relaxation of `FD-031` has a pointwise scale-sensitive gap from the unrestricted GCD-duality ray. For every fixed `0<lambda<1` there is `c_lambda>0` such that, uniformly for all prime-prefix cutoffs `Y` with `lambda H<=Y<H`, every admissible source satisfies

\[
\boxed{
R_H(a)
\le \widehat R_{H,D(H,Y)}
\le C_H-c_\lambda H^{-1/2}
\le \zeta(2)-c_\lambda H^{-1/2}
}
\tag{3}
\]

for all sufficiently large `H`.

This is the first pointwise quantitative separation in the linear-breadth Schur program. It is stronger than the `O(1/H)` finite truncation loss of the unrestricted constant `C_H`, but it still tends to zero and therefore does **not** by itself improve the Franel--Landau exponent or prove RH. Its main consequence is structural: the isolated cheap-alignment spikes left logically possible by `FD-035` cannot be arbitrarily sharp for the actual quotient-shell source.

## 1. The physical quotient-shell transform is exactly 1-Lipschitz

Retain the arithmetic function from `FD-033`,

\[
\mathcal H(X)
=\sum_{n\le X}c(n),
\qquad
c(n)=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}{n}.
\tag{4}
\]

Because `rad(n)<=n` and `phi(rad(n))<=rad(n)`,

\[
\boxed{|c(n)|\le1.}
\tag{5}
\]

Hence for all nonnegative integers `u,v`,

\[
\boxed{
|\mathcal H(u)-\mathcal H(v)|\le |u-v|.
}
\tag{6}
\]

No cancellation theorem is used here. Equation (6) is simply the bounded-increment property of the exact source already identified in `FD-033`.

Now retain the `FD-031`--`FD-034` notation. The physical Schur energy is

\[
E_{H,D}
=\sum_{r>D}w(r)
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2,
\qquad
w(r):=\frac{J_2(r)}{r^2},
\tag{7}
\]

and the distinguished Schur direction has Jordan coordinate

\[
-\frac{\mu(r)}{J_2(r)}
\qquad(r>D).
\tag{8}
\]

Let

\[
\Delta_{H,D}:=C_H-C_D,
\qquad
\tau_{H,D}:=\frac{\beta_{H,D}}{\Delta_{H,D}}.
\tag{9}
\]

Thus `tau` is the scalar giving the orthogonal projection of the physical tail onto the distinguished direction. Since

\[
\rho_{H,D}^2
=E_{H,D}-\frac{\beta_{H,D}^2}{\Delta_{H,D}}
=\varepsilon_{H,D}E_{H,D},
\tag{10}
\]

one has

\[
\boxed{
\tau_{H,D}^2
=\frac{E_{H,D}(1-\varepsilon_{H,D})}{\Delta_{H,D}}.
}
\tag{11}
\]

Also `Delta_(H,D)<=C_H<=Z`, where `Z=zeta(2)`.

In the exact Jordan-row norm, (10) implies for every `r>D`

\[
\boxed{
\left|
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)
+\tau_{H,D}\,\mu(r)\frac r{J_2(r)}
\right|
\le \sqrt{Z\varepsilon_{H,D}E_{H,D}}.
}
\tag{12}
\]

Indeed the left side squared is multiplied by `w(r)>=1/Z` inside the residual energy. At a nonsquarefree row, `mu(r)=0`, so (12) says directly that the corresponding quotient-shell value must be small whenever the projective defect is small.

## 2. A nearby squarefree/nonsquarefree row pair converts angle alignment into an energy bound

Fix once and for all an odd prime `ell>D`. We use only that `ell` is fixed while `H` grows. Suppose first that

\[
0<\varepsilon:=\varepsilon_{H,D}\le\frac12.
\tag{13}
\]

Choose a prime `q>ell`, and let

\[
q^*:=4\left\lceil\frac q4\right\rceil.
\tag{14}
\]

For odd `q`,

\[
1\le q^*-q\le3.
\tag{15}
\]

The row

\[
r=\ell q
\tag{16}
\]

is squarefree, whereas

\[
r^*=\ell q^*
\tag{17}
\]

is nonsquarefree because `4|q^*`. For all sufficiently large `H` both rows lie in `(D,H]` for the choices below.

By (11), `Delta<=Z`, and (13),

\[
|\tau_{H,D}|
\ge\sqrt{\frac{E_{H,D}}{2Z}}.
\tag{18}
\]

Since `w(r)<=1`, the squarefree target in (12) has magnitude at least

\[
\left|\tau_{H,D}\frac r{J_2(r)}\right|
=\frac{|\tau_{H,D}|}{r w(r)}
\ge
\frac{\sqrt{E_{H,D}}}{\ell q\sqrt{2Z}}.
\tag{19}
\]

On the other hand, the nonsquarefree target at `r^*` is exactly zero. Therefore, whenever

\[
q\sqrt\varepsilon\le\eta_D
\tag{20}
\]

for a sufficiently small fixed constant `eta_D>0`, the two row errors in (12) consume at most half of (19). Writing

\[
u=\left\lfloor\frac{H}{\ell q}\right\rfloor,
\qquad
v=\left\lfloor\frac{H}{\ell q^*}\right\rfloor,
\tag{21}
\]

we obtain

\[
\boxed{
|\mathcal H(u)-\mathcal H(v)|
\gg_D \frac{\sqrt{E_{H,D}}}{q}.
}
\tag{22}
\]

But the arguments are extremely close. Equations (15) and (21) give

\[
|u-v|
\le
\frac{3H}{\ell q^2}+1.
\tag{23}
\]

The exact Lipschitz law (6) now forces

\[
\boxed{
\sqrt{E_{H,D}}
\ll_D \frac Hq+q.
}
\tag{24}
\]

This is the new mechanism. Projective alignment wants a squarefree row to carry a quotient-shell value of size roughly `sqrt(E)/q`, while the adjacent nonsquarefree row wants value zero. The physical arithmetic source can change by at most one per unit of its quotient argument, and those two arguments differ by only `O(H/q^2)`. A sufficiently large aligned energy therefore cannot be hidden between the two rows.

## 3. The actual source obeys `E << H^2 epsilon`

We next choose `q` at the scale dictated by the defect. The already established bounds make this choice uniform.

First, `FD-034` gives the crude physical-energy ceiling

\[
E_{H,D}\le Z^3H^2.
\tag{25}
\]

Second, the terminal multiples-of-four argument of `FD-032` gives, for fixed `D` and all sufficiently large `H`,

\[
\rho_{H,D}^2
=\varepsilon E_{H,D}
\ge \frac{H}{16Z}.
\tag{26}
\]

Combining (25) and (26),

\[
\boxed{
\varepsilon\ge\frac{1}{16Z^4H}.
}
\tag{27}
\]

Now fix a sufficiently small constant `eta_D` satisfying (20), and in the small-defect regime set

\[
Q:=\frac{\eta_D}{\sqrt\varepsilon}.
\tag{28}
\]

For `Q` larger than a fixed threshold, the prime number theorem, already anchored in this research line, supplies a prime

\[
Q\le q\le2Q.
\tag{29}
\]

Taking the threshold above `ell` ensures that `ell q` is squarefree. If `Q` is below that threshold, then `epsilon` is bounded below by a fixed positive constant and the conclusion below follows immediately from (25), so only (29) is the nontrivial case.

By construction, `q sqrt(epsilon)<=2 eta_D`, so (20) holds after shrinking `eta_D` once. Equation (27) also implies `q=O_D(sqrt H)`, hence `r,r^*<=H` for large `H`. Substituting (29) into (24) gives

\[
\frac Hq\ll_D H\sqrt\varepsilon.
\tag{30}
\]

For the second term, (27) gives `H epsilon >> 1`, so

\[
q\ll_D\varepsilon^{-1/2}
\ll_D H\sqrt\varepsilon.
\tag{31}
\]

Therefore

\[
\boxed{
E_{H,D}\ll_D H^2\varepsilon_{H,D}.
}
\tag{32}
\]

Equation (32) is the physical-source regularity statement missing from the abstract control in `FD-035`. A sparse energy spike of size close to the quadratic ceiling cannot simultaneously have a tiny projective defect: the bounded increments of `mathcal H` force its neighboring squarefree and nonsquarefree rows to resolve that spike over too short a quotient interval.

## 4. The terminal transverse mass and the Lipschitz upper tradeoff meet at `H^{-1/2}`

Combining (26) with (32) gives

\[
\frac{H}{16Z}
\le
\varepsilon E_{H,D}
\ll_D H^2\varepsilon^2.
\tag{33}
\]

Hence

\[
\boxed{
\varepsilon_{H,D}\gg_D H^{-1/2},
}
\tag{34}
\]

which is (1).

The exponent `1/2` is not an asserted arithmetic transition. It is the balance delivered by the present two ingredients: a compulsory residual mass of order `H`, and the adjacent-row Lipschitz tradeoff `E<<H^2 epsilon`. Stronger short-interval control for `mathcal H`, or another relation coupling several neighboring row types at once, would be needed to improve this exponent by the same method.

The result is genuinely pointwise: no averaging over `4`-adic chains, density argument, monotonicity of `E`, or lower growth theorem such as `FD-033` is used. Thus it survives exactly the sparse-spike logical escape exhibited by `FD-035`, while remaining compatible with that finding because the abstract profile there was never required to satisfy (6) or the adjacent-row Jordan geometry.

## 5. Uniform consequence for every fixed positive linear prime breadth

Fix `0<lambda<1` and let

\[
D(H,Y)=\left\lfloor\frac{H}{Y+1}\right\rfloor,
\qquad
Y\ge\lambda H.
\tag{35}
\]

`FD-031` gives

\[
D(H,Y)\le
D_\lambda:=\left\lceil\frac1\lambda\right\rceil-1.
\tag{36}
\]

Choose the same odd prime `ell>D_lambda` in the preceding proof. All constants are then uniform over the finite set `1<=D<=D_lambda`, so

\[
\varepsilon_{H,D(H,Y)}\ge c_\lambda H^{-1/2}.
\tag{37}
\]

Moreover

\[
\Delta_{H,D}=C_H-C_D
\longrightarrow Z-C_D,
\tag{38}
\]

and the finite set of possible `D` gives a uniform positive lower bound for `Delta` once `H` is large. Since `FD-031` gives

\[
\widehat R_{H,D}
=C_H-\Delta_{H,D}\varepsilon_{H,D},
\tag{39}
\]

we obtain (3).

For the physical Möbius source itself one may take, for example, the half-linear regime `Y>=H/2`, where `D=1`. Using the exact `FD-003` Franel normalization,

\[
12\left(M_H\mathfrak F_H+\frac1{12}\right)
=m^TK_Hm,
\tag{40}
\]

there is therefore an absolute `c>0` such that

\[
\boxed{
|\mathbf M(H)|^2
\le
12\left(Z-cH^{-1/2}\right)
\left(M_H\mathfrak F_H+\frac1{12}\right)
}
\tag{41}
\]

for all sufficiently large `H`.

This improves the unrestricted finite-dimensional coefficient at a scale much larger than the generic `O(1/H)` truncation defect `Z-C_H`, but it is still only a multiplicative coefficient tending to `Z`. Equation (41) does not bound the size of the Franel energy itself and therefore does not improve the Mertens exponent.

## 6. Prior-art, scope, and falsification boundary

The proof is deliberately composed from already canonical local ingredients plus one elementary source property. The coefficient formula (4) is in `FD-033`; the Schur/Jordan row representation and the equality-direction coordinates are in `FD-034`; the terminal linear residual is in `FD-032`; and the crude quadratic energy ceiling is already in `FD-034`. The only external arithmetic input used in the new step is existence of a prime in `[Q,2Q]` for all sufficiently large `Q`, for which the prime number theorem already recorded in `SOURCES.md` is more than sufficient. No new load-bearing source is required.

A targeted prior-art search covered Farey/Franel discrepancy with Mertens functions, normalized GCD matrices and Jordan-totient decompositions, and the Dirichlet quotient `zeta(s+1)/zeta(s)`. It found the expected classical neighboring material but no external theorem needed for (6), (12), or the adjacent-row argument. No novelty is claimed for bounded increments of a summatory function, prime selection, GCD-matrix factorization, or Jordan totients in isolation. The line-specific delta is the exact splice yielding (32)--(34) for the physical Mertens tail under linear prime ancestry.

The main falsification checks are explicit. The row `ell q` must be squarefree, so `ell` and `q` are distinct primes; the threshold in (29) enforces this. The comparison row `ell q^*` is nonsquarefree because `4|q^*`, regardless of any other factor. The gap `q^*-q<=3` is what converts the physical one-step bound into the `H/q^2` quotient separation. The projection scale in (11) is used only after `epsilon<=1/2`; larger defects already satisfy (1) trivially for large `H`. Finally, the result gives a decaying `H^{-1/2}` pointwise gap, not a positive limiting gap, not a new asymptotic for `mathcal H`, and not an RH proof.

The next live question is correspondingly narrower. To turn the pointwise `H^{-1/2}` separation into a nonvanishing linear-prefix gap, one must add arithmetic information that beats the unit-increment resolution used here: a stronger short-interval law for the quotient-shell source, a coupled family of nearby squarefree/nonsquarefree rows whose errors cannot be paid independently, or an interaction with the exact longitudinal/endpoint channel of `FD-031`. Merely adding further separate prime-square renormalization inequalities remains blocked by `FD-035`.