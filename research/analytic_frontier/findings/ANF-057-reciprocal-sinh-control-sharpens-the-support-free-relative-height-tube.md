# ANF-057 — reciprocal-sinh control sharpens the support-free relative-height tube

**Status:** `EXACT-DERIVED + SUPPORT-FREE-HEIGHT-RATIO-TUBE + PROFILE-SPECIFIC-MARGIN-TRANSFER + MONTGOMERY-TAYLOR-RESIDUAL-SHRINKAGE + STRUCTURAL-REDUCTION`. `ANF-056` removes a fixed unequal-height neighborhood of the diagonal by retaining the positive quadratic mismatch block, but its elementary split loses part of the available diagonal margin. The exact mismatch loss admits a sharper global envelope once the relative height mismatch is above a small technical threshold. Combining that envelope with the diagonal margin of `ANF-054` enlarges the curvature-gated support-free tube and, using the strict Montgomery--Taylor curvature margin from `ANF-038`, enlarges it further for the live base-zero problem.

Let `J` be nonzero, continuous, even and nonnegative with compact support. Put

\[
K_J(t)=\int \alpha^2J(\alpha)\cos(2\pi\alpha t)\,d\alpha,
\qquad K_0=K_J(0)>0,
\]

\[
m_5(J)=2K_0+3\inf_tK_J(t),
\]

and assume the curvature gate

\[
\boxed{m_5(J)\ge0.}
\tag{1}
\]

For genuine heights `y_1,y_2>0`, write

\[
y=\frac{y_1+y_2}{2},
\qquad
\delta=\frac{|y_1-y_2|}{2},
\qquad
q=\frac{\delta}{y}\in[0,1).
\tag{2}
\]

Define

\[
r_J:=\frac{m_5(J)}{K_0}\ge0
\tag{3}
\]

and the profile-dependent threshold

\[
\boxed{
q_J:=\frac13(1+r_J)
\left(1-\sqrt{\frac{3}{8(1+r_J)}}\right).
}
\tag{4}
\]

Then every two-pair five-point configuration with

\[
\boxed{q<q_J}
\tag{5}
\]

is strictly safe for every horizontal placement:

\[
\boxed{H_J(y_1,y_2;t_1,t_2)>0.}
\tag{6}
\]

Since `q_J` is increasing in `r_J`, every profile satisfying the curvature gate (1) has the support-free radius

\[
\boxed{
q<q_*:=\frac13\left(1-\sqrt{\frac38}\right)
=0.1292091881\ldots
\quad\Longrightarrow\quad H_J>0.
}
\tag{7}
\]

Equivalently, every genuine zero or negative defect for a profile satisfying (1) must satisfy

\[
\boxed{
\frac{y_{\max}}{y_{\min}}
\ge\frac{1+q_*}{1-q_*}
=1.2967628650\ldots .
}
\tag{8}
\]

Within the curvature-gated profile class, this replaces the `q_c=0.10616522...` and height-ratio `1.23754...` of `ANF-056` by `q_*=0.12920918...` and `1.29676...`, without using a support radius or a bounded-height hypothesis.

For the exact Montgomery--Taylor profile, `ANF-038` certifies

\[
m_5(J_{\rm MT})>0.0078,
\qquad
K_0<0.1549985926411777.
\tag{9}
\]

Hence

\[
r_{\rm MT}>
\frac{0.0078}{0.1549985926411777},
\]

and direct outward-rounded substitution in (4) gives

\[
\boxed{q_{\rm MT}>0.1409.}
\tag{10}
\]

Therefore the accepted Montgomery--Taylor base-zero problem has the stronger exclusion

\[
\boxed{
H_{\rm MT}=0
\quad\Longrightarrow\quad
\frac{|y_1-y_2|}{y_1+y_2}>0.1409,
\qquad
\frac{y_{\max}}{y_{\min}}>1.3280.
}
\tag{11}
\]

The last remaining cardinality-five search is thus separated from the equal-height diagonal by a materially wider fixed cone than `ANF-056` supplied.

## 1. The exact mismatch loss from ANF-056

Retain the mean-height normal form of `ANF-055`--`ANF-056`. For a fixed frequency put

\[
U=2\pi|\alpha|y,
\qquad
V=2\pi|\alpha|\delta=qU,
\]

and

\[
x=\sinh U\,\sinh V=\sinh U\,\sinh(qU).
\tag{12}
\]

Equation (17) of `ANF-056` gives, uniformly over both horizontal variables,

\[
h_\alpha-h_\alpha^{\rm diag}
\ge4x^2-2x.
\tag{13}
\]

Consequently the whole negative part is bounded by

\[
\boxed{
\ell_q(U):=2x(1-2x)_+.
}
\tag{14}
\]

`ANF-056` used the uniform envelope `\ell_q(U)<=U^2/4` inside its certified range. The new step is to retain the dependence on `q`.

## 2. A reciprocal-sinh inequality controls the hyperbolic excess

For every `t>=0`,

\[
\boxed{
\frac{t}{\sinh t}\ge1-\frac{t^2}{6}.
}
\tag{15}
\]

For `t>=sqrt(6)` the right side is nonpositive. For `0<=t<sqrt(6)`, use

\[
\frac{\sinh t}{t}
=\sum_{n\ge0}\frac{t^{2n}}{(2n+1)!}
\le
\sum_{n\ge0}\frac{t^{2n}}{6^n}
=\frac1{1-t^2/6},
\tag{16}
\]

where `(2n+1)!>=6^n`; inversion gives (15).

For `U>0` define the hyperbolic excess ratio

\[
R(U,q):=\frac{x}{qU^2}
=\frac{\sinh U}{U}
\frac{\sinh(qU)}{qU}
\ge1.
\tag{17}
\]

Equation (15) yields the global estimate

\[
\boxed{
1-\frac1R
\le\frac{(1+q^2)U^2}{6}.
}
\tag{18}
\]

Indeed, if `(1+q^2)U^2>=6` this is immediate from `1-1/R<1`. Otherwise both quadratic lower bounds in (15) are positive, and

\[
\begin{aligned}
\frac1R
&=\frac{U}{\sinh U}\frac{qU}{\sinh(qU)}\\
&\ge
\left(1-\frac{U^2}{6}\right)
\left(1-\frac{q^2U^2}{6}\right)\\
&\ge1-\frac{(1+q^2)U^2}{6}.
\end{aligned}
\tag{19}
\]

Define

\[
q_0:=6-\sqrt{35}=0.0839202169\ldots .
\tag{20}
\]

For `q>=q_0`,

\[
\frac{1+q^2}{6}\le2q.
\tag{21}
\]

Combining (18)--(21),

\[
R-1
\le2qU^2R
\le2qU^2R^2.
\tag{22}
\]

If `x>=1/2`, then `\ell_q(U)=0`. If `x<1/2`, use `x=qU^2R` and (22):

\[
\begin{aligned}
\frac{\ell_q(U)}{2qU^2}
&=R\bigl(1-2qU^2R\bigr)\\
&\le1.
\end{aligned}
\]

Thus, for every `U>=0`,

\[
\boxed{
q\ge q_0
\quad\Longrightarrow\quad
\ell_q(U)\le2qU^2.
}
\tag{23}
\]

This is support free, scale free and pointwise in frequency.

## 3. Transfer the diagonal curvature margin

From (13)--(14) and (23), whenever `q>=q_0`,

\[
h_\alpha-h_\alpha^{\rm diag}
\ge-2qU^2
=-8\pi^2q\alpha^2y^2.
\tag{24}
\]

Integrating against `J>=0` gives

\[
\boxed{
H_J(y_1,y_2;t_1,t_2)
\ge
H_J(y,y;t_1,t_2)
-8\pi^2qK_0y^2.
}
\tag{25}
\]

Under the explicit curvature-gate hypothesis (1), `ANF-054` supplies the profile-dependent all-horizontal diagonal margin

\[
H_J(y,y;t_1,t_2)
\ge
\frac{8\pi^2}{3}(K_0+m_5)
\left(1-\sqrt{\frac{3K_0}{8(K_0+m_5)}}\right)y^2.
\tag{26}
\]

Using `r_J=m_5/K_0`, equations (25)--(26) become

\[
\boxed{
H_J
\ge8\pi^2K_0y^2\,(q_J-q)
\qquad(q\ge q_0).
}
\tag{27}
\]

Hence every `q_0<=q<q_J` is strictly safe.

There is no gap below `q_0`: `ANF-056` already proves strict positivity for

\[
q\le q_c
=\operatorname{arsinh}\!\left(\frac1{8\sinh1}\right)
=0.10616522\ldots,
\]

and `q_0<q_c`. Since `q_J>=q_*>q_c`, the two estimates join to prove (5)--(7) for the entire interval from the exact diagonal up to `q_J`.

The function in (4) is increasing in `r_J>=0`, so its minimum over profiles satisfying (1) is attained at `r_J=0`, yielding exactly (7).

## 4. The new coefficient is small-height sharp for this horizontal-free route

The improvement is not just a better arbitrary split. As `U->0`,

\[
x=qU^2+O_q(U^4),
\]

and therefore

\[
\boxed{
\ell_q(U)=2qU^2+O_q(U^4).
}
\tag{28}
\]

Thus the coefficient `2q` in (23) cannot be lowered in any envelope that is uniform down to zero frequency and depends only on `(q,U)` through the exact mismatch loss (14). Consequently the threshold `q_J` is the natural endpoint of **this particular comparison** between the all-horizontal mismatch loss and the `ANF-054` diagonal lower margin.

This does not make `q_J` the true positivity radius. The exact mismatch identity still contains the discarded positive term `4sinh^2(V)C^2`, and the true diagonal defect can exceed the lower bound (26). A further extension must therefore retain horizontal phase/separation information, use a stronger profile-specific diagonal margin, or analyze the fixed Montgomery--Taylor integral directly. Merely re-optimizing the scalar split of `ANF-056` cannot improve the small-frequency coefficient in (28).

## 5. Consequence for the live Montgomery--Taylor zero problem

For `J_MT`, (10)--(11) remove the full relative mismatch range

\[
0\le q\le0.1409.
\tag{29}
\]

This combines usefully with `ANF-049`, which says any negative configuration must also satisfy

\[
2\sinh\!\left(\frac{2\pi y}{3|d|}\right)
\sinh\!\left(\frac{2\pi qy}{3|d|}\right)<1,
\qquad d=t_1-t_2.
\tag{30}
\]

Hence any surviving zero or negative witness is simultaneously bounded **away from the diagonal** by (11) and forced back toward it relative to the horizontal separation by (30). The residual shape domain is an intermediate mismatch band rather than a neighborhood of `y_1=y_2`.

For example, inserting the certified lower bound `q>0.1409` into (30) already forces the mean height to be smaller than about three quarters of the pair-center separation; this is only a corollary of the exact hyperbolic condition and is not used in the theorem. The more useful next gate is to keep (30) in exact form while attacking the remaining fixed `J_MT` integral.

## 6. Stress tests, prior art, and evidence boundary

The proof has three short audit points. First, (15) follows coefficientwise from `(2n+1)!>=6^n` and needs no numerical approximation. Second, (18) must be checked separately in the regimes `(1+q^2)U^2>=6` and `<6`; the latter uses the product of the two reciprocal-sinh lower bounds, not a one-sided Taylor truncation for `sinh`. Third, (23) follows from the exact algebra `x=qU^2R`; its small-`U` limit (28) is a direct falsification check on every constant.

The numerical Montgomery--Taylor specialization uses only the rigorous intervals already persisted in `ANF-038`; the rounded value `0.1409` is below the lower endpoint obtained by substituting those intervals in the monotone formula (4). No sampled minimization or floating-point sign decision is evidence for (10).

A targeted prior-art check of current Montgomery--Taylor/pair-correlation work and the positive-definite-strip Fourier--Laplace literature recovered the same established extremal and representation frameworks already anchored in `SOURCES.md`, but did not identify an external theorem giving the two-pair mean-height mismatch inequality (13), the reciprocal-sinh transfer (23), or the resulting profile-dependent radius (4). The elementary inequality (15) is standard analysis; the durable derived content is its use inside the exact five-point mismatch normal form. No publication-level novelty claim is made and no new source anchor is load-bearing, so `SOURCES.md` is unchanged.

This finding remains a sufficient positivity theorem for profiles satisfying the curvature gate (1). It does not decide the unequal-height Montgomery--Taylor region beyond (11), does not prove the full universal affine certificate, and does not address larger conjugation-invariant multisets. Its role is to shrink the exact decision problem accepted in `CLUE-central-notch-base-margin-certificate` before any interval or phase-aware certification is attempted.