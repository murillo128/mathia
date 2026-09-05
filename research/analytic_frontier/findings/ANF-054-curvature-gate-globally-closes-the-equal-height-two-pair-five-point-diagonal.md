# ANF-054 — the curvature gate globally closes the equal-height two-pair five-point diagonal

**Status:** `EXACT-DERIVED + GLOBAL-EQUAL-HEIGHT-CLOSURE + QUANTITATIVE-MARGIN + CURVATURE-COHERENCE-TRANSFER + STRUCTURAL-REDUCTION`. `ANF-050` proves a bandwidth-only safe radius on the equal-height diagonal but leaves anti-phase frequencies pointwise dangerous beyond that radius. `ANF-053` then reduces survival of the central-notch family to zero-freeness of the fixed Montgomery--Taylor two-pair defect. The equal-height part of that remaining problem can in fact be closed globally without using the special Montgomery--Taylor formula.

Let `J` be nonzero, continuous, even, nonnegative and compactly supported, put

\[
K_J(t):=\int \alpha^2J(\alpha)\cos(2\pi\alpha t)\,d\alpha,
\qquad K_0:=K_J(0)>0,
\]

and retain the five-point curvature margin

\[
m_5(J):=2K_0+3\inf_tK_J(t).
\tag{1}
\]

If

\[
\boxed{m_5(J)\ge0,}
\tag{2}
\]

then for every common height `y>0` and every horizontal placement,

\[
\boxed{
H_J(y,y;t_1,t_2)>0.
}
\tag{3}
\]

More quantitatively,

\[
\boxed{
H_J(y,y;t_1,t_2)
\ge
\frac{8\pi^2y^2}{3}\,(K_0+m_5(J))
\left(
1-\sqrt{\frac{3K_0}{8(K_0+m_5(J))}}
\right).
}
\tag{4}
\]

In particular the curvature gate alone gives the uniform horizontal margin

\[
\boxed{
H_J(y,y;t_1,t_2)
\ge
\frac{8\pi^2}{3}
\left(1-\sqrt{\frac38}\right)K_0y^2
>0.
}
\tag{5}
\]

Thus the frequencywise anti-phase danger found in `ANF-042` and `ANF-050` cannot align strongly enough across the spectrum once the same second-moment curvature profile passes `m_5>=0`.

## 1. Equal heights factor the residual block through one anti-phase cosine

Use the Hilbert normal form of `ANF-045`--`ANF-047`. For fixed relative separation

\[
d:=t_1-t_2,
\]

write the common-translation parameterization as `(t_1,t_2)=(t+d,t)`. At frequency `alpha` put

\[
u:=2\pi\alpha y,
\qquad
a(\alpha):=\cosh u-1,
\qquad
C(\alpha):=\cos(\pi\alpha d).
\tag{6}
\]

On the equal-height diagonal the shape amplitude from `ANF-045` is

\[
u_d(\alpha)
=a(\alpha)e^{2\pi i\alpha d}+a(\alpha)
=2a(\alpha)e^{\pi i\alpha d}C(\alpha).
\tag{7}
\]

Therefore its positive residual block `B:=Q+P` becomes

\[
\begin{aligned}
B
&=4\int J(\alpha)a(\alpha)(a(\alpha)+2)C(\alpha)^2\,d\alpha\\
&=\boxed{
4\int J(\alpha)\sinh^2(2\pi\alpha y)
\cos^2(\pi\alpha d)\,d\alpha.
}
\end{aligned}
\tag{8}
\]

The only potentially negative common-translation term is

\[
Z(t)=\int J(\alpha)e^{2\pi i\alpha t}u_d(\alpha)\,d\alpha,
\]

so

\[
H_J=B+\operatorname{Re}Z(t).
\tag{9}
\]

As in the phase-blind envelope of `ANF-047`, define

\[
L:=\int J|u_d|
=2\int J(\alpha)a(\alpha)|C(\alpha)|\,d\alpha.
\tag{10}
\]

Then `|Z(t)|<=L`, hence

\[
H_J\ge B-L.
\tag{11}
\]

The new point is that on equal heights the curvature gate itself forces `L` to be a strict fraction of `B`.

## 2. Weighted Cauchy converts the hyperbolic linear term into self-energy

Because `a>=0`, weighted Cauchy--Schwarz gives

\[
\begin{aligned}
\left(\frac L2\right)^2
&=\left(\int J\,
\sqrt{a(a+2)}\,|C|\,
\sqrt{\frac{a}{a+2}}\right)^2\\
&\le
\left(\int J a(a+2)C^2\right)
\left(\int J\frac{a}{a+2}\right).
\end{aligned}
\tag{12}
\]

Using (8), put

\[
R_y:=\int J(\alpha)\frac{a(\alpha)}{a(\alpha)+2}\,d\alpha.
\tag{13}
\]

Then

\[
\boxed{L^2\le B R_y.}
\tag{14}
\]

The ratio in (13) has the exact hyperbolic form

\[
\frac{a}{a+2}
=\frac{\cosh u-1}{\cosh u+1}
=\tanh^2\!\left(\frac u2\right).
\tag{15}
\]

Since `|tanh x|<=|x|` for real `x`,

\[
\boxed{
R_y
\le
\pi^2y^2\int\alpha^2J(\alpha)\,d\alpha
=\pi^2y^2K_0.
}
\tag{16}
\]

No small-height approximation is being made: (15) is exact and the elementary `tanh` bound holds at every height.

## 3. The same curvature kernel gives a uniform lower bound for the residual block

From `sinh^2 u>=u^2` and (8),

\[
\begin{aligned}
B
&\ge
16\pi^2y^2
\int \alpha^2J(\alpha)\cos^2(\pi\alpha d)\,d\alpha\\
&=8\pi^2y^2\bigl(K_0+K_J(d)\bigr).
\end{aligned}
\tag{17}
\]

Let

\[
k_*:=\inf_tK_J(t).
\]

Equation (1) gives

\[
K_0+k_*
=\frac{K_0+m_5(J)}3.
\tag{18}
\]

Hence

\[
\boxed{
B
\ge
\frac{8\pi^2y^2}{3}\bigl(K_0+m_5(J)\bigr).
}
\tag{19}
\]

Combining (16) and (19),

\[
\boxed{
\frac{R_y}{B}
\le
\frac{3K_0}{8(K_0+m_5(J))}
\le\frac38,
}
\tag{20}
\]

where the final inequality uses `m_5(J)>=0`.

Now (14) and (20) imply

\[
L
\le
B\sqrt{\frac{3K_0}{8(K_0+m_5(J))}}
\le
\sqrt{\frac38}\,B.
\tag{21}
\]

Substituting this in (11) proves (4), and dropping the nonnegative `m_5` from the resulting monotone lower envelope gives (5).

The proof also shows why the pointwise danger tube is not contradictory. Near an anti-phase frequency `C(alpha)=0`, the linear amplitude can be locally more dangerous than the positive block, exactly as `ANF-050` records. But the weighted average of `C^2` is

\[
\int \alpha^2J(\alpha)C(\alpha)^2\,d\alpha
=\frac{K_0+K_J(d)}2
\ge\frac{K_0}{6},
\tag{22}
\]

under `m_5>=0`. The spectrum therefore cannot sit coherently enough near anti-phase to defeat the integrated hyperbolic self-energy.

## 4. Montgomery--Taylor has a uniform all-horizontal diagonal margin

For the exact Montgomery--Taylor spectrum, `ANF-038` gives

\[
m_5(J_{\rm MT})>0.0078
\]

and

\[
K_0
=\int\alpha^2J_{\rm MT}(\alpha)\,d\alpha
>0.1549985926411760.
\tag{23}
\]

Already the universal version (5) therefore yields the simple certified bound

\[
\boxed{
H_{\rm MT}(y,y;t_1,t_2)>1.58\,y^2
\qquad(y>0,\ t_1,t_2\in\mathbb R).
}
\tag{24}
\]

The constant `1.58` is deliberately rounded down; direct substitution of the lower endpoint in (23) into (5) gives more than `1.5812`.

Consequently the base-profile zero problem of `ANF-053` has **no solution on the equal-height diagonal**, at any horizontal separation or common translation. This is stronger than the bandwidth radius of `ANF-050`: even when individual frequencies enter its exact anti-phase danger tube, the full Montgomery--Taylor integral remains uniformly positive.

The same theorem applies to every sufficiently narrow central-notch separator for which `ANF-038`--`ANF-039` retain `m_5(J_s)>0`. Thus equal-height two-pair configurations cannot be the five-point obstruction for that family either.

## 5. Structural consequence for the accepted base-margin clue

The accepted `CLUE-central-notch-base-margin-certificate` asks whether `H_MT` has any genuine zero after the compactness, balance and anti-phase reductions of `ANF-044`--`ANF-053`. Equation (24) removes the exact diagonal from that search with a quantitative margin independent of all horizontal variables.

Hence any remaining Montgomery--Taylor zero must satisfy

\[
\boxed{y_1\ne y_2.}
\tag{25}
\]

At the same time `ANF-049` shows that a negative defect, and therefore any first zero reached from the positive small-height region, cannot have strongly unbalanced heights. The residual geometry is therefore not the equal-height core itself: it is an **intermediate mismatch layer** inside the existing height-balance cone.

On any fixed compact obstruction box with heights bounded below by `epsilon>0`, the explicit diagonal margin (5) plus uniform continuity also excludes some open tube around `y_1=y_2`. No numerical tube width is claimed here because the compactification constants in the current canon were not made explicit. A complete base-margin certificate still has to control the remaining unequal-height region or produce a rigorous zero there.

## 6. Prior art, falsification, and evidence boundary

The load-bearing external framework is unchanged. Complex Fourier--Laplace representation of positive-definite strip kernels is classical and already anchored in `SOURCES.md` through Buescu--Paixão--Symeonides; Cauchy--Schwarz and the elementary hyperbolic inequalities used above are standard. A targeted search of that strip-positive-definite literature and the reproducing-kernel pair-correlation literature found the expected representation theory but no theorem matching the equal-height five-point inequality (3)--(5). No publication-level novelty claim is made, and no new `SOURCES.md` entry is required because the result is derived directly from the local `ANF-045` normal form and the already canonical curvature gate.

The decisive audit is short. Expanding (7) must give the equal-height specialization of `ANF-045`; (8) follows from `a(a+2)=sinh^2 u`; weighted Cauchy must give exactly `L^2<=BR_y`; and `cos^2(pi alpha d)=(1+cos(2pi alpha d))/2` must turn the lower bound for `B` into (17). A counterexample to the theorem would therefore require either a spectrum with `m_5(J)>=0` and an equal-height configuration violating (3), or an error in one of those four identities. Numerical searches are not evidence for the theorem and are not used in its proof.

The result is deliberately limited to the exact diagonal `y_1=y_2`. It does not prove a global unequal-height neighborhood without additional quantitative continuity control, does not decide the accepted Montgomery--Taylor zero-freeness clue, and does not address larger multisets. Its durable contribution is to convert what had remained a pointwise-dangerous equal-height anti-phase branch into a globally positive branch under the same curvature condition already required by the rest of the five-point program.
