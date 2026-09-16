# PC-321 — large Mordell–Tornheim exponent is zero-free on the right polyhalf-plane

**Status:** `EXACT-DERIVED` + `LITERATURE-AUDITED` + `DECISIVE-BOUNDARY` for the large-`u` regime of the canonical `(5,7)` nonlinear Prime-Circle packet from PC-316.

PC-319 and PC-320 show that the canonical Mordell–Tornheim carrier

\[
Z_{5,7}(s,t,u)
=\sum_{k,l\ge1}\frac{a_5(k)b_7(l)}{k^s l^t(k+l)^u}
\tag{1}
\]

has off-critical zeros throughout a neighborhood of the decoupled face `u=0`. A surviving possibility was that a distinguished positive-coupling regime bounded away from that face might have qualitatively different zero geometry.

There is now an exact obstruction at the opposite end. For the same canonical source pair,

\[
\boxed{
Z_{5,7}(s,t,u)\neq0
\qquad
(\Re s\ge0,\ \Re t\ge0,\ \Re u\ge5).
}
\tag{2}
\]

Thus the entire strong-`u` polyhalf-plane is zero-free, including all points with `Re(s)=1/2` or `Re(t)=1/2`. Any RH-facing zero-selection mechanism inside this particular Mordell–Tornheim packet must therefore live at finite intermediate `u`; it cannot be obtained as a strong-additive-exponent limit.

## 1. A general first-output-mode dominance lemma

Let `a(k),b(l)` be bounded coefficient sequences with

\[
|a(k)|\le M_a,\qquad |b(l)|\le M_b,
\tag{3}
\]

and define

\[
Z_{a,b}(s,t,u)
:=\sum_{k,l\ge1}\frac{a(k)b(l)}{k^s l^t(k+l)^u}.
\tag{4}
\]

For `Re(u)>2` the series converges absolutely whenever `Re(s),Re(t)>=0`. The unique pair with minimal output frequency `k+l=2` is `(k,l)=(1,1)`. Scaling by `2^u` therefore gives

\[
2^u Z_{a,b}(s,t,u)
=a(1)b(1)+R(s,t,u),
\tag{5}
\]

where, on the closed right polyhalf-plane,

\[
\begin{aligned}
|R(s,t,u)|
&\le M_aM_b
\sum_{(k,l)\ne(1,1)}
\left(\frac{2}{k+l}\right)^{\Re u}\\
&=M_aM_b E(\Re u),
\end{aligned}
\tag{6}
\]

with

\[
E(v):=\sum_{n=3}^{\infty}(n-1)\left(\frac2n\right)^v.
\tag{7}
\]

The function `E(v)` is decreasing and tends to zero. Hence every bounded two-source packet with `a(1)b(1) != 0` has a source-dependent zero-free strong-`u` half-space once

\[
M_aM_b E(\Re u)<|a(1)b(1)|.
\tag{8}
\]

This is not a consequence of absolute convergence alone. It comes from the unique smallest additive output mode and the fact that increasing `Re(u)` suppresses every other pair relative to `(1,1)`.

## 2. The canonical `(5,7)` source gives an explicit threshold

PC-319 records the canonical Fourier packets. With

\[
\omega=e^{-2\pi i/5},\qquad \xi=e^{-2\pi i/7},
\tag{9}
\]

we have

\[
a_5(k)=
\begin{cases}
\omega^{3k},&5\nmid k,\\
0,&5\mid k,
\end{cases}
\qquad |a_5(k)|\le1,
\tag{10}
\]

and

\[
b_7(l)=
\begin{cases}
\frac12(\xi^{3l}+\xi^{5l}),&7\nmid l,\\
0,&7\mid l,
\end{cases}
\qquad |b_7(l)|\le1.
\tag{11}
\]

The leading coefficient is nonzero and has the exact modulus

\[
|a_5(1)b_7(1)|
=\left|\frac{\xi^3+\xi^5}{2}\right|
=\cos\frac{2\pi}{7}
>\frac12,
\tag{12}
\]

because `0<2*pi/7<pi/3`.

It remains only to bound `E(5)`. Put

\[
f(x)=\frac{x-1}{x^5}=x^{-4}-x^{-5},
\tag{13}
\]

which is positive and decreasing for `x>=3`. Then

\[
\begin{aligned}
E(5)
&=32\sum_{n=3}^{\infty}\frac{n-1}{n^5}\\
&\le32\left[
\frac{2}{3^5}+\frac{3}{4^5}
+\int_4^\infty(x^{-4}-x^{-5})\,dx
\right]\\
&=\frac{1915}{3888}
<\frac12.
\end{aligned}
\tag{14}
\]

Since `E(v)` decreases with `v`, equations (6), (12), and (14) imply for every

\[
\Re s\ge0,\qquad \Re t\ge0,\qquad \Re u\ge5
\tag{15}
\]

that

\[
\left|2^uZ_{5,7}(s,t,u)-a_5(1)b_7(1)\right|
<\frac12
<|a_5(1)b_7(1)|.
\tag{16}
\]

The reverse triangle inequality proves (2). No continuation, numerical root search, simplicity assumption, or asymptotic interchange is involved.

## 3. What this does to the PC-319/PC-320 escape

PC-319 gives genuinely coupled off-critical zeros for every sufficiently small positive real `u`. PC-320 strengthens that to a full local zero hypersurface near the decoupled face. Equation (2) supplies the opposite boundary: by `Re(u)=5` the same canonical packet is uniformly zero-free on the complete right `(s,t)` polyhalf-plane.

Therefore an RH-facing proposal based on choosing a positive `u` cannot appeal to either endpoint regime. Near `u=0` the packet provably carries zeros already in `Re(s)>1`; for `Re(u)>=5` it carries no zeros at all for `Re(s),Re(t)>=0`. A hypothetical distinguished zero-selective slice must be justified by an additional source-forced theorem at an intermediate value or locus of `u`, and must explain why that finite regime is geometrically selected. Merely taking the additive exponent to be large does the opposite of producing a Riemann-like divisor: it collapses the packet to its unique lowest output-frequency coefficient.

This does **not** prove that every finite `0<Re(u)<5` slice has off-critical zeros, nor does it rule out a determinant/quotient or a different nonlinear geometry. It rules out the strong-`u` limit and gives an explicit zero-free barrier for the canonical pair that generated PC-319/PC-320.

## 4. Prior-art and novelty audit

The analytic destination remains the classical Mordell–Tornheim family already identified in PC-316. Toma's 2025 treatment derives Mordell–Tornheim multiple Dirichlet-series representations and functional equations by Mellin–Barnes methods (Yuichiro Toma, *International Journal of Number Theory* 21:9 (2025), 2171–2183, DOI `10.1142/S1793042125501052`). Nakamura proves that a neighboring Tornheim–Hurwitz family can have nontrivial zeros even in a region of absolute convergence (Takashi Nakamura, *Monatshefte für Mathematik* 162 (2011), 167–178, DOI `10.1007/s00605-009-0164-5`). Thus neither the function class nor absolute convergence supplies the zero-free conclusion above.

No novelty is claimed for first-term domination of a convergent Dirichlet-type series. The Mathia-specific content is the exact application to the canonical Prime-Circle `(5,7)` coefficient packet, where the geometry supplies a unique minimal additive mode, the source gives the explicit nonzero coefficient `cos(2*pi/7)`, and the elementary bound yields the concrete zero-free polyhalf-plane `Re(u)>=5`.

A directed prior-art search for Mordell–Tornheim zero-free regions at large additive exponent did not locate this exact canonical coefficient statement. That absence is not treated as a historical novelty claim.

## 5. Audit tests and evidence boundary

The result can be falsified locally without computation:

1. Verify the canonical coefficient formulas (10)--(11) from the centered prime-support sources at levels `5` and `7`.
2. Verify that `(1,1)` is the unique pair with `k+l=2` and that every other pair contributes to (7) with `n>=3`.
3. On `Re(s),Re(t)>=0`, check `|k^{-s}l^{-t}|<=1` and hence the uniform remainder bound (6).
4. Check the decreasing-integral estimate in (14) and the strict inequalities `1915/3888<1/2<cos(2*pi/7)`.
5. Apply the reverse triangle inequality to obtain (2).

The finding establishes only a zero-free **large-additive-exponent region** for the canonical PC-316 packet and the general dominance criterion (8). It does not identify a special intermediate exponent, a functional equation, a determinant with new zeros, or any implication for RH.