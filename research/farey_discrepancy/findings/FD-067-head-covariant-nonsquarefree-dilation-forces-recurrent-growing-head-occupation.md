# FD-067 — head-covariant nonsquarefree dilation forces recurrent growing-head occupation

**Status:** `EXACT-DERIVED + HEAD-COVARIANT-DILATION + GROWING-SCHUR-HEAD + JOINT-NONSQUAREFREE-OCCUPATION + ZERO-FRONTIER-CALIBRATED + MULTISCALE-OBSTRUCTION`.

`FD-047` shows, for a fixed Schur head `D`, that every nonsquarefree dilation imports a complete lower-horizon copy of the physical Jordan energy into the nonsquarefree rows. `FD-065` then shows that allowing `D` to grow improves denominator-side occupation estimates but loses scalar Schur leverage. There is a stronger exact relation between these two facts: the dilation itself also rescales the head.

For every nonsquarefree integer `q>1`, every horizon `H`, and every `1<=D<H`, one has

\[
\boxed{
U_{H,D}
\ge
w(q)E_{\lfloor H/q\rfloor,\lfloor D/q\rfloor},
\qquad
w(q):=\frac{J_2(q)}{q^2}.
}
\tag{1}
\]

Thus a growing head does not destroy the multiplicative renormalization law. Along a `q`-adic horizon chain, any head schedule satisfying

\[
\left\lfloor\frac{D_j}{q}\right\rfloor\le D_{j-1}
\tag{2}
\]

still gives an exactly telescoping lower bound for the **actual joint nonsquarefree occupation**. Polynomial heads `D_j=H_j^{\delta+o(1)}` with `0<=delta<=1` admit such schedules. If

\[
a_\delta(\Theta):=\delta+2\Theta(1-\delta),
\]

then the zero-frontier envelope implies

\[
\boxed{
\liminf_{n\to\infty}
\left(
\prod_{j=1}^n
\frac{U_{H_j,D_j}}{E_{H_j,D_j}}
\right)^{1/n}
\ge
w(q)q^{-a_\delta(\Theta)}.
}
\tag{3}
\]

For `q=4`, this interpolates from the fixed-head `FD-047` constant `(3/4)4^(-2Theta)` to the **Theta-independent** linear-head constant `3/16`. More importantly for the Schur relaxation, on a positive lower proportion of every such multiplicative chain the scalar loss satisfies

\[
\boxed{
\mathfrak D_{H_j,D_j}
\gg \frac1{D_j}
=H_j^{-\delta+o(1)}.
}
\tag{4}
\]

The result does not yield a pointwise gap and does not cross the direct-transfer barrier of `FD-066`: a sparse sequence may still jump between multiplicative rays. It does show that **head growth cannot create an all-scale escape inside any fixed nonsquarefree dilation chain**. Once the head is transported covariantly, the recurrent scalar loss is limited only by the intrinsic leverage `Delta_(H,D) asymp 1/D`, rather than by the larger generic zero-frontier denominator exponent.

## 1. The square-divisor injection rescales the cutoff as well as the horizon

Retain the physical quantities

\[
E_{H,D}
:=
\sum_{D<r\le H}
w(r)
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2,
\]

\[
U_{H,D}
:=
\sum_{\substack{D<r\le H\\\mu(r)=0}}
w(r)
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2,
\qquad
w(r)=\frac{J_2(r)}{r^2},
\tag{5}
\]

and put

\[
H':=\left\lfloor\frac Hq\right\rfloor,
\qquad
D':=\left\lfloor\frac Dq\right\rfloor.
\tag{6}
\]

Let `q` be nonsquarefree. For every integer `s` with

\[
D'<s\le H',
\tag{7}
\]

the row `r=qs` obeys `D<r<=H` and is nonsquarefree. The floor quotient is exactly

\[
\boxed{
\left\lfloor\frac{H}{qs}\right\rfloor
=
\left\lfloor\frac{H'}s\right\rfloor.
}
\tag{8}
\]

Indeed, write `H=qH'+a` with `0<=a<q`; after division by `qs`, the extra term `a/(qs)` is too small to cross the next `1/s` grid step.

The Jordan weight satisfies the multiplicative overlap inequality

\[
\boxed{w(qs)\ge w(q)w(s),}
\tag{9}
\]

because every Euler factor `1-p^(-2)` appearing in both `q` and `s` is counted once on the left and twice on the right. The injection `s -> qs`, restricted to the rows (7), therefore gives

\[
\begin{aligned}
U_{H,D}
&\ge
\sum_{D'<s\le H'}
 w(qs)
 \mathcal H\!\left(\left\lfloor\frac{H}{qs}\right\rfloor\right)^2\\
&\ge
w(q)
\sum_{D'<s\le H'}
 w(s)
 \mathcal H\!\left(\left\lfloor\frac{H'}s\right\rfloor\right)^2,
\end{aligned}
\]

which is exactly (1).

This strictly strengthens the cutoff bookkeeping in `FD-034` and `FD-047`. Those findings retained the same `D` at the lower horizon, using only rows `s>D`. The physical row condition is merely `qs>D`, so the full imported copy starts already at `s>floor(D/q)`.

Since the Schur equality ray vanishes on every nonsquarefree Jordan row, `FD-032`/`FD-065` also give

\[
\rho_{H,D}^2\ge U_{H,D},
\qquad
\varepsilon_{H,D}:=\frac{\rho_{H,D}^2}{E_{H,D}}
\ge
\nu_{H,D}:=\frac{U_{H,D}}{E_{H,D}}.
\tag{10}
\]

Thus the head-covariant injection controls both the joint occupation and the larger projective defect.

## 2. Subcovariant head schedules telescope exactly

Fix a nonsquarefree `q` and an integer `H_0>=1`, and set

\[
H_j=q^jH_0.
\tag{11}
\]

Let `D_j` be any integer head schedule with `1<=D_j<H_j` for all sufficiently large `j` and satisfying (2). Since `E_(H,D)` is nonincreasing in `D`, equation (1) gives

\[
\begin{aligned}
U_{H_j,D_j}
&\ge
w(q)
E_{H_{j-1},\lfloor D_j/q\rfloor}\\
&\ge
w(q)E_{H_{j-1},D_{j-1}}.
\end{aligned}
\tag{12}
\]

Writing

\[
E_j:=E_{H_j,D_j},
\qquad
U_j:=U_{H_j,D_j},
\qquad
\nu_j:=\frac{U_j}{E_j},
\tag{13}
\]

we obtain the exact product inequality

\[
\boxed{
\prod_{j=1}^n\nu_j
\ge
w(q)^n\frac{E_0}{E_n}.
}
\tag{14}
\]

No comparison between unrelated head sizes is used after (12); the denominator telescopes with the same moving head that defines the numerator at each scale.

The condition (2) includes the natural polynomial schedules. If

\[
D_j=\left\lfloor cH_j^\delta\right\rfloor,
\qquad
0<\delta\le1,
\tag{15}
\]

then

\[
\frac{D_j}{q}
\le
c q^{\delta-1}H_{j-1}^\delta
\le
cH_{j-1}^\delta,
\]

so (2) holds after taking floors. The case `delta=0` is the fixed-head regime already used in `FD-047`. More generally, bounded multiplicative perturbations may be admitted whenever the explicit inequality (2) is checked; the power exponent alone is not a substitute for that covariance condition.

## 3. Zero-frontier calibration for polynomial heads

Let

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\tag{16}
\]

For every fixed `sigma>Theta`, the source envelope from `FD-046`, used for growing heads in `FD-065`, gives

\[
E_{H,D}
\ll_\sigma
H^{2\sigma}D^{1-2\sigma}.
\tag{17}
\]

Suppose the head schedule in Section 2 additionally satisfies

\[
D_j=H_j^{\delta+o(1)},
\qquad
0\le\delta\le1.
\tag{18}
\]

Then

\[
E_n
\ll
H_n^{\,\delta+2\sigma(1-\delta)+o(1)}.
\tag{19}
\]

Because `H_n=q^nH_0`, taking `n`th roots in (14), then letting `sigma` decrease to `Theta`, yields

\[
\boxed{
\liminf_{n\to\infty}
\left(\prod_{j=1}^n\nu_j\right)^{1/n}
\ge
w(q)q^{-a_\delta(\Theta)},
}
\tag{20}
\]

where

\[
\boxed{
a_\delta(\Theta)=\delta+2\Theta(1-\delta).}
\tag{21}
\]

The same bound holds with `epsilon_j` in place of `nu_j` by (10). For `delta=0`, (20) is exactly the fixed-head zero-frontier calibration of `FD-047`. At `delta=1`, the zero-frontier exponent cancels:

\[
\boxed{
a_1(\Theta)=1.}
\tag{22}
\]

For `q=4`, `w(4)=3/4`, so

\[
\boxed{
\liminf_{n\to\infty}
\left(\prod_{j=1}^n\nu_j\right)^{1/n}
\ge
\frac34\,4^{-\{\delta+2\Theta(1-\delta)\}}.
}
\tag{23}
\]

At a linear head this is `3/16` for every possible `Theta`. Using only `1/2<=Theta<=1`, the unconditional worst-case interpolation is

\[
\boxed{
\frac34\,4^{-a_\delta(\Theta)}
\ge
\frac{3}{4^{3-\delta}}.
}
\tag{24}
\]

Thus the guaranteed four-adic geometric-mean occupation improves continuously from `3/64` at a fixed/subpower head to `3/16` at a linear head. This is a statement about recurrent occupation along the complete chain, not about monotonicity of the pointwise ratio in `D`.

## 4. The lower tail gives recurrent scalar gaps limited only by Schur leverage

The product estimate controls more than the arithmetic mean. Put

\[
L_{q,\delta}
:=
a_\delta(\Theta)\log q-\log w(q).
\tag{25}
\]

Since `0<nu_j<=1`, equation (20) implies

\[
\limsup_{n\to\infty}
\frac1n\sum_{j=1}^n\log\frac1{\nu_j}
\le L_{q,\delta}.
\tag{26}
\]

Hence for every `0<eta<1`,

\[
\boxed{
\limsup_{n\to\infty}
\frac1n
\#\{1\le j\le n:\nu_j\le\eta\}
\le
\frac{L_{q,\delta}}{\log(1/\eta)}.
}
\tag{27}
\]

If

\[
\eta<w(q)q^{-a_\delta(\Theta)},
\tag{28}
\]

the right-hand side of (27) is strictly below one. Therefore a positive lower proportion of the chain satisfies `nu_j>eta`, and hence also `epsilon_j>eta`.

For the scalar Schur loss

\[
\mathfrak D_{H,D}
=
\Delta_{H,D}\varepsilon_{H,D},
\qquad
\Delta_{H,D}=C_H-C_D,
\tag{29}
\]

`FD-065` proves

\[
\Delta_{H,D}\asymp D^{-1}
\tag{30}
\]

whenever `D->infinity` and `2D<H`; for a fixed head, `Delta` instead tends to the positive constant `zeta(2)-C_D`. Consequently, for polynomial schedules with `0<delta<1`, and also for `delta=1` when the proportionality constant in (15) is less than `1/2`, every `eta` satisfying (28) gives a positive lower proportion of indices with

\[
\boxed{
\mathfrak D_{H_j,D_j}
\gg_\eta D_j^{-1}
=H_j^{-\delta+o(1)}.
}
\tag{31}
\]

This is stronger on those recurrent scales than the generic pointwise terminal estimate from `FD-065`. With `D=H^{delta+o(1)}`, that pointwise mechanism has scalar-loss exponent

\[
\tau_\delta
=(2\Theta-1)+2\delta(1-\Theta)
=\delta+(2\Theta-1)(1-\delta).
\tag{32}
\]

Thus, when `Theta>1/2` and `delta<1`, the recurrent chain bound (31) saves the additional power

\[
\boxed{\tau_\delta-\delta=(2\Theta-1)(1-\delta)>0.}
\tag{33}
\]

relative to the generic pointwise denominator normalization. Under RH the two exponents coincide, as they should. The gain in (33) is not a new pointwise estimate: it is the price of retaining the exact multiplicative recurrence rather than bounding every horizon independently.

## 5. What this changes, and what it does not

`FD-065` establishes that simply moving the Schur head outward cannot improve the **pointwise scalar** packet mechanism, because denominator savings are overpaid by the loss `Delta asymp 1/D`. Equation (1) shows that this conclusion should not be interpreted as loss of the underlying nonsquarefree geometry. If the horizon and head are followed together through a fixed multiplicative chain, the nonsquarefree union recursively sees the entire preceding physical tail, including the newly exposed rows between `D/q` and `D`.

This sharpens the surviving escape in two ways. First, a growing head cannot make `U/E` small on essentially every member of a fixed nonsquarefree dilation chain. Second, after multiplying by Schur leverage, a positive lower proportion of those scales have scalar loss of order at least `1/D`, with no extra zero-frontier power penalty. For false `Theta>1/2`, this is polynomially stronger than the all-horizon terminal estimate on those scales.

It does **not** solve the fixed-head pointwise occupation clue. `FD-035` already permits isolated low-defect horizons under the separate recurrence data, and (27) likewise permits sparse exceptional members of every chain. More importantly, a zero-frontier spike sequence may select different multiplicative rays at successive scales. Nothing here forces the adaptive spikes of `FD-046`/`FD-066` to intersect the positive-density good set of one fixed `q`-adic chain. The direct-transfer `ell>2(1-Theta)` barrier is therefore untouched.

Nor does a recurrent gap for the relaxed Schur quotient by itself improve the Franel--Landau exponent. The exact implication remains at the level of the linear-prefix relaxation: it classifies another way in which projective saturation can fail, and narrows a successful escape to **cross-ray intermittency or additional source/denominator coupling**, rather than mere growth of the Schur cut.

## 6. Prior-art boundary and falsification checks

The divisor-incidence/Jordan factorization underlying the Schur coordinates belongs to the classical Smith GCD-matrix literature already anchored in `SOURCES.md`, and the zero-frontier envelope is the classical Mertens/zeta input already anchored there through Titchmarsh. A targeted literature audit across GCD/meet matrices, Jordan-totient factorizations, Farey--Mertens discrepancy formulas, and recent Farey discrepancy work found the expected matrix and local-discrepancy structures, but no statement matching the moving-cutoff inequality (1) or its growing-head multiplicative-chain consequence (20). No priority claim is made: the row injection itself is elementary, and the durable contribution here is the Mathia-specific combination with the physical Schur cutoff and zero-frontier energy.

No new external theorem is load-bearing, so `SOURCES.md` requires no change.

The main checks are exact. Nonsquarefreeness of `q` is essential: otherwise the image `qs` is not always a transverse row. The cutoff must scale as `floor(D/q)`; replacing it by a larger cutoff is valid but weaker, while replacing it by a smaller one would include rows whose images need not exceed `D`. The schedule condition (2) is what makes the moving-head product telescope; merely knowing `D_j=H_j^{delta+o(1)}` without multiplicative control is insufficient. Finally, (20) uses only an upper envelope for `E_n`, so it is a lower bound on chain occupation, not an assertion that the physical energy has the displayed exact growth exponent.

A counterexample to (1), (12), or the floor/weight identities would refute the exact claim. A sparse sequence with `U/E -> 0` chosen across different multiplicative rays would **not** refute it and remains an admitted escape. The next genuinely different step would need a mechanism that couples those rays or localizes zero-frontier spikes relative to the recurrent good sets; repeating the same dilation on more fixed chains does not supply that bridge.