# NB-041 — the logarithmic zero-loss tail coordinate has a shrinking Möbius dual selector

**Status:** `EXACT-DERIVED + SOURCE-DEFINED-DUAL-SELECTOR + LOG-MOBIUS-PRIOR-ART + N-UNIFORM-TAIL-MOMENT-LOCKING + SHRINKING-DUAL-NORM + ORACLE-BOUNDARY-REFINEMENT`. `NB-040` identifies the one extra coefficient coordinate needed by the exact zero-loss weighted-skeleton quotient,
\[
\sigma_{M,N}(a)=\sum_{n=M}^{N}\frac{a_n}{n}\log\frac nM,
\]
and shows that for the optimal coefficient vector its exact value participates in an identity containing `1-d_N^2`. That makes exact recovery of the coordinate potentially target-oracular. The coordinate nevertheless admits an explicit source-defined ambient dual whose norm tends to zero. In fact, using current explicit estimates for the logarithmically mollified Möbius sum, the dual norm is `O(1/log M)`, uniformly in the upper section `N`.

Use the canonical generators
\[
g_n(x)=\left\{\frac1{nx}\right\}-\frac1n\left\{\frac1x\right\},
\qquad
V_N=\operatorname{span}(g_2,\ldots,g_N),
\qquad e(x)=1,
\tag{1}
\]
and the bounded step-tail selectors `\Psi_L` from `NB-035`,
\[
\langle e,\Psi_L\rangle=m(L),
\qquad
\langle g_n,\Psi_L\rangle=
\begin{cases}
0,&2\le n\le L,\\
1/n,&n>L,
\end{cases}
\tag{2}
\]
where
\[
m(x):=\sum_{n\le x}\frac{\mu(n)}n.
\tag{3}
\]

For `M>=2`, put
\[
\delta_L:=\log\frac{L+1}{L}
\tag{4}
\]
and define the explicit vector
\[
\boxed{
\Omega_M
:=
e-\sum_{L=1}^{M-1}\delta_L\Psi_L.
}
\tag{5}
\]

Then for every integer `n>=2`,
\[
\boxed{
\langle g_n,\Omega_M\rangle=
\begin{cases}
0,&n\le M,\\[1mm]
\dfrac1n\log\dfrac nM,&n>M.
\end{cases}
}
\tag{6}
\]

Define the classical logarithmically mollified Möbius sum
\[
\check m(x)
:=
\sum_{n\le x}\frac{\mu(n)}n\log\frac xn
\tag{7}
\]
and its defect from the value selected at `s=1`,
\[
\boxed{
\Theta(x):=1-\check m(x).
}
\tag{8}
\]

The target pairing of the dual is exactly
\[
\boxed{
\langle e,\Omega_M\rangle=\Theta(M).
}
\tag{9}
\]

Consequently, for **every** finite canonical approximant
\[
v_N=\sum_{n=2}^{N}a_ng_n,
\qquad
r=e-v_N,
\qquad N\ge M,
\tag{10}
\]
the `NB-040` logarithmic tail coordinate satisfies
\[
\boxed{
\left|
\sigma_{M,N}(a)-\Theta(M)
\right|
\le
\|\Omega_M\|\,\|r\|.
}
\tag{11}
\]

Moreover,
\[
\boxed{
\|\Omega_M\|\ll\frac1{\log M}
}
\qquad(M\to\infty),
\tag{12}
\]
with an absolute effective implied constant. Hence for the canonical best approximant
\[
p_N=P_{V_N}e=\sum_{n=2}^{N}a_{N,n}g_n,
\qquad
d_N=\|e-p_N\|,
\tag{13}
\]
one has the `N`-uniform source lock
\[
\boxed{
\sigma_{M,N}(a_N)
=
\Theta(M)
+
O\!\left(\frac{d_N}{\log M}\right)
}
\qquad(N\ge M),
\tag{14}
\]
and, since `d_N<=1` and `\Theta(M)=O(1/\log M)`,
\[
\boxed{
\sup_{N\ge M}
\left|\sigma_{M,N}(a_N)\right|
\ll
\frac1{\log M}.
}
\tag{15}
\]

Thus the extra logarithmic coefficient coordinate isolated by `NB-040` is not an uncontrolled scalar at coarse absolute scale: it has a source-only Möbius prediction and a stability constant that **shrinks** with the cutoff. What remains target-oracular is exact/Burnol-scale recovery and, more importantly, the geometric realization of the unique weighted-tail target line `P_{\widehat W_{M,N}}e`.

## 1. The logarithmic coordinate is an exact cumulative step-tail dual

From (2),
\[
\sum_{L=1}^{M-1}\delta_L
\langle g_n,\Psi_L\rangle
=
\frac1n
\sum_{L=1}^{\min(M-1,n-1)}
\delta_L.
\tag{16}
\]
The logarithms telescope:
\[
\sum_{L=1}^{K}\delta_L=\log(K+1).
\tag{17}
\]
Since the canonical target pairing is
\[
\langle e,g_n\rangle=\frac{\log n}{n},
\tag{18}
\]
equations (5), (16), and (17) prove (6).

For the target,
\[
\begin{aligned}
\sum_{L=1}^{M-1}\delta_Lm(L)
&=
\sum_{n<M}\frac{\mu(n)}n
\sum_{L=n}^{M-1}\delta_L\\
&=
\sum_{n<M}\frac{\mu(n)}n\log\frac Mn\\
&=
\check m(M),
\end{aligned}
\tag{19}
\]
because the omitted `n=M` term is zero. This proves (9).

Equation (6) then gives, for every coefficient vector,
\[
\langle v_N,\Omega_M\rangle
=
\sum_{n=M+1}^{N}\frac{a_n}{n}\log\frac nM
=
\sigma_{M,N}(a),
\tag{20}
\]
where the `n=M` term in the `NB-040` definition also vanishes. Therefore
\[
\Theta(M)-\sigma_{M,N}(a)
=
\langle r,\Omega_M\rangle,
\tag{21}
\]
and Cauchy--Schwarz proves (11).

There is also an equivalent Vasyunin form. `NB-036` proves
\[
\xi_n=n(\Psi_{n-1}-\Psi_n).
\tag{22}
\]
A second telescoping gives
\[
\boxed{
\Omega_M
=
e
-
\sum_{n=2}^{M-1}\frac{\log n}{n}\xi_n
-
\log M\,\Psi_{M-1}.
}
\tag{23}
\]
Thus the new selector is not a second biorthogonal system. It is the precise logarithmic cumulative combination of the Vasyunin duals and the bounded endpoint selector required to read the `NB-040` coordinate.

## 2. Exact shell formula and the shrinking norm

Let
\[
I_t=\left(\frac1{t+1},\frac1t\right].
\tag{24}
\]
The `NB-035` shell formula for `\Psi_L` gives, after summing (5) in `L`,
\[
\boxed{
\Omega_M|_{I_t}
=
\begin{cases}
(t+1)\Theta(M/t)-t\Theta(M/(t+1)),&1\le t<M,\\
1,&t\ge M.
\end{cases}
}
\tag{25}
\]

For completeness, the first line follows from
\[
\sum_{L=t}^{M-1}
\delta_L\,
m\!\left(\left\lfloor\frac Lt\right\rfloor\right)
=
\sum_{k<M/t}\frac{\mu(k)}k
\log\frac{M}{tk}
=
\check m(M/t),
\tag{26}
\]
and the analogous identity with `t+1`.

The mollified sum is continuous and satisfies
\[
\check m(x)-\check m(y)
=
\int_y^x m(u)\,\frac{du}{u},
\qquad 1\le y\le x,
\tag{27}
\]
hence
\[
\Theta(x)-\Theta(y)
=
-\int_y^x m(u)\,\frac{du}{u}.
\tag{28}
\]
Writing the first line of (25) as
\[
\Omega_M|_{I_t}
=
\Theta(M/t)
+
t\left[
\Theta(M/t)-\Theta(M/(t+1))
\right]
\tag{29}
\]
shows directly how the shell size is controlled by one value of the mollified Möbius defect and one short logarithmic average of `m`.

The current explicit literature gives exactly the bounds needed here. Ramaré--Zuniga-Alterman, with an appendix by Balazard, prove for `x>=1`
\[
0\le\check m(x)\le1.00303,
\tag{30}
\]
and for sufficiently large `x`
\[
|\Theta(x)|\ll\frac1{\log x},
\qquad
|m(x)|\ll\frac1{\log x}.
\tag{31}
\]
Their published constants include `|\Theta(x)|<=0.043/log x` for `x>=10^14` and the explicit reciprocal-Möbius estimate recorded in their Lemma 5.1. The finite argument of `NB-035` also gives the global bound `|m(x)|<=1`.

It follows from (28)--(31) that
\[
|\Omega_M|_{I_t}|\le2
\tag{32}
\]
for all `t<M`, while uniformly for `t<=\sqrt M`,
\[
|\Omega_M|_{I_t}|
\ll\frac1{\log M}.
\tag{33}
\]
Indeed, throughout the short interval
\[
\frac{M}{t+1}\le u\le\frac Mt
\tag{34}
\]
the arguments are at least a fixed multiple of `\sqrt M`, and
\[
t\log\frac{t+1}{t}\le1.
\tag{35}
\]

Since `|I_t|=1/(t(t+1))`, split the norm at `t=\lfloor\sqrt M\rfloor`. The early shells give
\[
\sum_{t\le\sqrt M}
\frac{|\Omega_M|_{I_t}|^2}{t(t+1)}
\ll\frac1{\log^2 M},
\tag{36}
\]
the remaining finite shells give
\[
\sum_{\sqrt M<t<M}
\frac{|\Omega_M|_{I_t}|^2}{t(t+1)}
\ll M^{-1/2},
\tag{37}
\]
and the region `t>=M`, namely `(0,1/M]`, contributes exactly
\[
\frac1M.
\tag{38}
\]
Thus
\[
\|\Omega_M\|^2
\ll
\frac1{\log^2 M}+M^{-1/2},
\tag{39}
\]
which proves (12).

The support tail in (38) also gives the unavoidable lower bound
\[
\boxed{
\|\Omega_M\|\ge M^{-1/2}.
}
\tag{40}
\]
No claim is made that the `O(1/log M)` upper bound is sharp.

## 3. Consequences for the zero-loss weighted-skeleton oracle

For the optimal residual, (11)--(12) prove (14). Ramaré--Zuniga-Alterman's estimate for the same mollified sum gives
\[
\Theta(M)=O(1/\log M),
\tag{41}
\]
and `d_N<=1`, so (15) follows uniformly over **all** upper sections `N>=M`.

This materially refines the interpretation of `NB-040`. Its exact identity
\[
\sigma_{M,N}(a_N)
=
1-d_N^2
-
\sum_{n=2}^{M-1}\frac{a_{N,n}\log n}{n}
-
\frac{\log M}{M}\tau_{M,N}
\tag{42}
\]
is still correct and still shows that exact values cannot simply be declared independently of the full target problem. But the same coordinate has an independent source-side dual representation (5) whose optimal value is asymptotically forced into an `O(1/log M)` window without knowing `d_N` or solving the upper section.

Equivalently, because every `\Psi_L` with `L<M` lies in the early-shell observation space `E_M`,
\[
\Omega_M-e\in E_M.
\tag{43}
\]
Hence the target-augmented observation space of `NB-040` may be written exactly as
\[
\boxed{
E_M+\operatorname{span}(e)
=
E_M+\operatorname{span}(\Omega_M).
}
\tag{44}
\]
This gives a completely source-defined representative of the one extra observation **modulo the already retained early-shell data**.

It does **not** make the unique geometric repair direction cheap:
\[
P_{\widehat W_{M,N}}\Omega_M
=
P_{\widehat W_{M,N}}e.
\tag{45}
\]
Computing that projection still recovers the same target-selected line identified in `NB-040`. Likewise, the `O(1/log M)` scalar control does not meet the accepted clue's `o(1/log N)` Burnol-scale target for every merely superlogarithmic cutoff `M/log N->infinity`; for example, `M=(log N)^2` only gives `1/log M` scale. The missing full metric/source-aligned defect of `NB-036`--`NB-039` is untouched.

## 4. Adversarial checks and boundary cases

The construction is independent of the upper section `N`. In particular, `M=N` gives `\sigma_{M,M}=0` and (11) reduces to the valid annihilator certificate
\[
|\Theta(M)|\le d_M\|\Omega_M\|.
\tag{46}
\]
This is a genuine target-aware dual lower bound, but no claim is made that it improves Burnol's zero-sensitive asymptotic lower bound.

The endpoint `M=2` is also exact:
\[
\Omega_2=e-\log2\,\Psi_1,
\tag{47}
\]
which annihilates `g_2` and pairs with every `g_n`, `n>2`, as `\log(n/2)/n`.

The shrinking norm uses arithmetic cancellation. The triangle inequality applied directly to (5) would only give `O(log M)` because `\|\Psi_L\|` is uniformly bounded and `\sum_{L<M}\delta_L=\log M`. Equation (25) is therefore essential: it converts the apparently growing positive combination into the mollified Möbius defects `m` and `\Theta`. Replacing those by absolute values before the shell resummation destroys the result.

No density assumption for the Nyman span is used. The exact dual identities (5)--(29) are finite. The only asymptotic input in (12) is unconditional Möbius cancellation already available from the prime number theorem, here made quantitative by the cited explicit estimates.

## 5. Prior art and research consequence

The arithmetic function `\check m(x)=\sum_{n\le x}\mu(n)n^{-1}\log(x/n)` is not new. Ramaré--Zuniga-Alterman explicitly study this logarithmically smoothed Möbius sum, including its non-negativity and quantitative approximation to `1`; those estimates are treated here as prior art and are now anchored in `SOURCES.md`. Vasyunin's biorthogonal family and the `NB-035` step-tail selector are also already prior art/line-local inputs as recorded in `NB-036`.

The line-local contribution is the exact identification of the `NB-040` zero-loss logarithmic coordinate with the ambient selector `\Omega_M`, the shell resummation (25), and the resulting `N`-uniform shrinking stability (14)--(15). This shifts the current oracle boundary. The extra coefficient scalar is asymptotically source-controlled; the hard part that survives is recovering the target-selected **geometry** or the Burnol-scale directional metric correction without an `N`-scale projection solve.

The accepted weighted-skeleton target-data clue therefore remains open, but its decisive test should no longer treat `\sigma_{M,N}` as wholly uncontrolled. Any next construction should use (14) as the source-side scalar baseline and spend its effort on the projected repair direction, the defect matrix/correlation pair, or a one-sided target certificate at the `o(1/log N)` scale.
