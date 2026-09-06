# XF-074 — Gaussian reference quotient is intrinsically local and cannot be a global Vieta carrier

**Status:** `EXACT-DERIVED` + `MATCHED-ZERO-FREE-CONTROL` + `THETA-SEAM-OBSTRUCTION` + `LOCALIZATION/BOUNDARY`. XF-073 proves that Gaussian/Appell periodization recovers the actual Xi heat solution with relative error `exp(-c (log T)^(9/2))` on the interior high-line segment `|Re z|<=L_T/4`. The remaining temptation is to feed the periodic quotient

\[
R_L=\frac{V_L}{W_L}
\]

directly into the global periodic Vieta/Parseval machinery of XF-067--XF-071.

That shortcut is false even for a zero-free exact heat solution. The periodized Gaussian reference has an exact vertical lattice of seam zeros

\[
\boxed{
z_{r,n}
=\left(r+\frac12\right)L
+i(2n+1)\frac{\pi v}{L},
\qquad r,n\in\mathbb Z,
}
\tag{1}
\]

where `v=sigma^2 h`. More strongly, at every frozen heat time there is a zero-free Fourier-mode solution of backward heat for which division by the reference turns **every one of these reference zeros into a genuine pole of `R_L`**. Thus reference division cancels the artificial Gaussian divisor for the special control `u=1`, but it does not produce a globally holomorphic periodic carrier for generic heat data.

At the Xi scaling of XF-073,

\[
L=(\log T)^3,
\qquad
v=(\log T)^{3/2}+O(1),
\]

the vertical seam spacing is

\[
\boxed{
\frac{2\pi v}{L}
=\Theta((\log T)^{-3/2}).
}
\tag{2}
\]

Consequently every full-period horizontal contour comes within `pi v/L` of a reference zero at the seam. The interior half-period used by XF-073 remains safe because it stays a horizontal distance `L/4` from that seam, but no global periodic holomorphic strip of macroscopic width survives.

This does **not** kill the Gaussian-reference route. It specifies what the next bridge may and may not do: it must remain center-local, explicitly quotient a meromorphic divisor with seam-residue control, or first construct a finite entire trigonometric surrogate whose auxiliary reference divisor is separately neutralized. What is ruled out is the direct identification of `R_L` with the entire periodic zero carrier required by XF-067--XF-071.

## 1. The periodized Gaussian has an exact seam-zero lattice

Keep the notation of XF-073. At a fixed heat time,

\[
h=1-\frac{2t}{\sigma^2},
\qquad
v=\sigma^2h>0,
\]

and suppress the harmless factor `h^{-1/2}`. Write

\[
\Theta_{L,v}(z)
:=
\sum_{m\in\mathbb Z}
\exp\!\left(-\frac{(z+mL)^2}{2v}\right),
\qquad
W_L=h^{-1/2}\Theta_{L,v}.
\tag{3}
\]

The sum converges normally on compact sets. It is `L`-periodic and obeys the exact imaginary quasi-periodicity

\[
\boxed{
\Theta_{L,v}\!\left(z+\frac{2\pi i v}{L}\right)
=
\exp\!\left(
\frac{2\pi^2v}{L^2}-\frac{2\pi iz}{L}
\right)
\Theta_{L,v}(z).
}
\tag{4}
\]

Indeed, shifting `z` by `2 pi i v/L` multiplies every summand by the same factor because `exp(-2 pi i m)=1`.

Now put

\[
z_n:=\frac L2+i(2n+1)\frac{\pi v}{L}.
\tag{5}
\]

Pair the summand with index `m` with the one of index `-m-1`. If

\[
a_m=\left(m+\frac12\right)L,
\]

then at `z_n`

\[
\frac{
\exp(-(-a_m+i\,\Im z_n)^2/(2v))
}{
\exp(-(a_m+i\,\Im z_n)^2/(2v))
}
=
\exp\!\left(
2i a_m\frac{\Im z_n}{v}
\right)
=-1.
\tag{6}
\]

Every pair therefore cancels exactly, proving

\[
\boxed{
\Theta_{L,v}(z_n)=0
\qquad(n\in\mathbb Z).
}
\tag{7}
\]

Horizontal periodicity gives the full family (1). This is the standard Jacobi-theta seam-zero pattern, but no theta zero theorem is needed for (7): the zeros used here follow directly from the Gaussian image sum.

The complementary even-height seam points are nonzero. On the real axis,

\[
\Theta_{L,v}(L/2)
=
\sum_m e^{-((m+1/2)L)^2/(2v)}>0.
\tag{8}
\]

Repeated use of (4) then gives

\[
\boxed{
\Theta_{L,v}\!\left(
\frac L2+i2n\frac{\pi v}{L}
\right)\ne0
\qquad(n\in\mathbb Z).
}
\tag{9}
\]

Equations (7)--(9), rather than any completeness statement about all theta zeros, are enough for the obstruction below.

## 2. A zero-free exact heat mode becomes meromorphic after reference division

The cancellation control `u\equiv1` in XF-073 is deliberately special: then `V_L=W_L` and `R_L\equiv1`. To stress-test whether this cancellation persists for generic heat data, use the exact zero-free backward-heat solution

\[
\boxed{
u_\omega(z,s)=e^{\omega^2s+i\omega z},
\qquad
(u_\omega)_s=-(u_\omega)_{zz}.
}
\tag{10}
\]

Its Gaussian/Appell transform can be completed to a square exactly. Using `v=sigma^2 h` and `t=sigma^2(1-h)/2`,

\[
\begin{aligned}
V_\omega(z,t)
&=
h^{-1/2}
 e^{-z^2/(2v)}
 e^{\omega^2t/h+i\omega z/h}\\
&=
e^{-\omega^2\sigma^2/2}
 h^{-1/2}
 \exp\!\left(
 -\frac{(z-i\omega\sigma^2)^2}{2v}
 \right).
\end{aligned}
\tag{11}
\]

Periodization therefore gives the exact identity

\[
\boxed{
V_{\omega,L}(z,t)
=
e^{-\omega^2\sigma^2/2}
W_L(z-i\omega\sigma^2,t),
}
\tag{12}
\]

and hence

\[
\boxed{
R_{\omega,L}(z,t)
=
e^{-\omega^2\sigma^2/2}
\frac{W_L(z-i\omega\sigma^2,t)}{W_L(z,t)}.
}
\tag{13}
\]

Freeze any time `t=t_0` and put

\[
\omega_0:=\frac{\pi h(t_0)}{L}.
\tag{14}
\]

Then

\[
\omega_0\sigma^2
=\frac{\pi v(t_0)}L.
\tag{15}
\]

At every reference zero `z_{r,n}` from (1), the numerator in (13) is evaluated at the corresponding even-height seam point

\[
z_{r,n}-i\omega_0\sigma^2
=
\left(r+\frac12\right)L
+i2n\frac{\pi v(t_0)}L,
\tag{16}
\]

which is nonzero by (9). Therefore

\[
\boxed{
R_{\omega_0,L}(\cdot,t_0)
\text{ has a genuine pole at every }z_{r,n},
}
\tag{17}
\]

even though the unperiodized input `u_{omega_0}` is entire and zero-free.

This is a matched architectural control, not an Xi-specific pathology. The artificial global divisor is created by **periodize then divide**, not inherited from zeros of the original heat solution.

## 3. The forced quotient equation is globally singular at exactly the wrong seam

XF-073 derives

\[
(R_L)_t
=-(R_L)_{zz}
-2\frac{(W_L)_z}{W_L}(R_L)_z.
\tag{18}
\]

The drift coefficient is meromorphic at every point (1), independently of the numerator. For special data such as `u=1`, the product with `(R_L)_z` has a removable cancellation because `R_L` is constant. Equation (17) shows that this is not a property of the operator on generic exact heat data.

Now return to the Xi scaling

\[
\ell=\log T,
\qquad
\sigma^2=\ell^{3/2},
\qquad
L=\ell^3,
\qquad
0\le t\le t_*.
\tag{19}
\]

Uniformly on that fixed interval,

\[
v=\ell^{3/2}-2t
=\ell^{3/2}(1+o(1)).
\tag{20}
\]

Given any horizontal height `y`, choose `n` so that

\[
\left|
y-(2n+1)\frac{\pi v}{L}
\right|
\le\frac{\pi v}{L}.
\tag{21}
\]

A full real period necessarily contains the seam point `x=L/2 mod L`, and hence

\[
\boxed{
\operatorname{dist}\!\left(
\{x+iy:x\in[0,L]\},
Z(W_L)
\right)
\le
\frac{\pi v}{L}
=
\Theta(\ell^{-3/2}).
}
\tag{22}
\]

Thus there is no full-period horizontal contour carrying a zero-free complex tube wider than `O((log T)^(-3/2))` for the reference. In contrast, the XF-073 interior contour `|Re z|<=L/4` stays a horizontal distance at least `L/4` from every exhibited seam zero, so its relative source estimate is untouched.

The distinction is exactly the one needed here: **local relative accuracy does not imply a globally holomorphic periodic quotient**.

## 4. Why this blocks the direct XF-067--XF-071 shortcut

The periodic Vieta carrier in XF-067 is an entire finite trigonometric heat solution

\[
G(z)=A\sum_{k=0}^N(-1)^kE_k e^{\pi i(N-2k)z/L},
\tag{23}
\]

whose degree-`N` zero divisor modulo `L` is encoded by a polynomial in `e^{2 pi i z/L}`. XF-070 then applies full-period center Parseval to the associated finite root multiset, and XF-071 transports its logarithmic Vieta quotient.

The quotient `R_L` in (13) belongs to a different analytic category: it is generally meromorphic, and even zero-free heat data can produce an infinite artificial zero-pole divisor at the reference seam. Therefore the formal move

\[
\text{interior Xi}\approx R_L
\quad\Longrightarrow\quad
\text{treat }R_L\text{ as the XF-067 periodic zero carrier}
\tag{24}
\]

is invalid. Its global logarithmic coefficients would encode the artificial theta divisor as well as the local heat data, and a root-only Vieta polynomial cannot represent the poles.

Nor does the super-small error in XF-073 repair this automatically. That estimate is deliberately restricted to `|Re z|<=L/4`, while all poles in the matched control lie at `Re z=L/2 mod L`. The theorem gives no estimate across the missing quarter-period on either side, and equation (17) proves that no source-independent holomorphic continuation statement can fill that gap.

This is a different obstruction from XF-072. XF-072 shows that moving a generic **root-block seam** farther away loses the same `1/R` in the full-period frame. XF-074 shows that the Gaussian-reference repair avoids that local source error but creates a **meromorphic reference seam** if one subsequently globalizes the quotient. The two findings leave the same architectural fork from opposite sides: a successful bridge must exploit genuinely local analytic information rather than silently returning to an unqualified full-period zero carrier.

## 5. Stress tests and evidence boundary

The control `u=1` still passes exactly: `V_L=W_L` and the quotient is identically one. XF-074 does not reinterpret the reference zeros as physical zeros in that case. It shows that this cancellation is not stable across the class of exact heat solutions.

There are also commensurate Fourier modes for which the vertical shift `omega sigma^2` happens to be an integer multiple of the reference quasi-period at one frozen time; their theta divisors can cancel. This is nongeneric and does not provide a fixed-time-interval mechanism because `v(t)=sigma^2-2t` changes with `t`. The explicit choice (14) instead forces maximal half-period misalignment and gives the clean pole witness (17).

No claim is made that the actual Xi numerator fails to vanish at every reference zero. Such a statement would require new global Xi information exactly where XF-073 intentionally avoids the seam. The stronger source-independent fact needed for the architectural conclusion is already available: the drift in (18) is meromorphic there, and a matched zero-free heat solution produces genuine poles. Hence cancellation cannot be assumed as part of a general destination-stability theorem.

The classical component is only the periodized-Gaussian/Jacobi-theta seam structure. The line-specific content is the matched backward-heat control (10)--(17), its Xi-scale consequence (22), and the resulting incompatibility with direct global Vieta transport. A prior-art check against standard Jacobi-theta zero and quasi-periodicity references found the theta lattice itself to be classical, but not this source/destination obstruction. The proof above is self-contained, so no new load-bearing bibliography entry is required.

## 6. Consequence for `xi_flow`

XF-073 genuinely closes the **local source periodization** gate, but it does not supply the global periodic carrier needed by XF-067--XF-071. The Gaussian route remains live only after making that locality explicit.

There are three mathematically distinct next options. One can build a center-local destination frame that never crosses `Re z=L/2`; one can keep the meromorphic quotient and prove a pole-subtracted weighted theorem with explicit control of seam residues; or one can truncate/renormalize an entire periodic heat object before division and prove that the auxiliary reference divisor does not pollute the guarded log-Vieta resource. Each option has a concrete falsifier and none is provided by XF-073 itself.

Until one of those bridges is proved, the accepted Gaussian-reference clue should remain open. XF-074 gives no upper bound on `Lambda` and no consequence for RH by itself.