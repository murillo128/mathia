# MI-008 — Small real notches admit an exact simple/double reduction

**Evidence level:** supported by the analytic derivation in
[ANF-213](../../findings/ANF-213-small-real-notch-minima-reduce-exactly-to-simple-and-double-sites.md).
The particle-removal mechanism is classical; no novelty or complex-zero
consequence is inferred.

Use the Fourier convention `f_hat(x)=int f(u)e^(-2pi iux)du`, and put

\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\quad F=\widehat g^{\,2},\quad
\Phi_\eta(x)=\eta\operatorname{sinc}^2(\eta x),\quad
V=F-a\Phi_\eta,\quad A=V(0)=1-a\eta.
\]

Here `sinc(t)=sin(pi t)/(pi t)`, `0<eta<=1/2`, `0<a<=1/100`.
For distinct real sites `x_i` of positive integer multiplicity `m_i`, let

\[
E=\sum_{i,j}m_im_jV(x_i-x_j),\quad
L=\sum_i\ell(m_i),\quad
\ell(0)=0,\ \ell(1)=1,\ \ell(m)=2m\ (m\ge2),\quad Q=E/L.
\]

Every nonempty finite multiset `W` has a nonempty submultiset `Z` at the
same sites with `Q(Z)<=Q(W)`, multiplicities only `1,2`, and

\[
M(Z):=\max_y\sum_{x_i\in[y,y+1/4)}m_i\le4.
\]

Thus restricting to this class preserves the **actual real infimum**;
it is not an approximate clipping theorem or an assumed pair ansatz.

The useful proof has two local estimates independent of total cardinality:
`F(x)>=1/2` for `|x|<=1/4`, and
`sum_j m_j Phi_eta(y-x_j)<=7M(W)` for every real `y`. For the second,
partition into quarter-length cells and sum the full tail majorant
`min(eta,1/(pi^2 eta x^2))`. Its integral cancels the apparent width loss.
Replacing the tail by its height would incorrectly charge all particles.

Choose a submultiset minimizing `Q`; its value `q` is at most `A`.
If `P_i=sum_j m_j V(x_i-x_j)`, removing one copy loses

\[
D_i=2P_i-A,\qquad d_i=\ell(m_i)-\ell(m_i-1)
=\begin{cases}1&m_i=1,\\3&m_i=2,\\2&m_i\ge3.\end{cases}
\]

Optimality requires `D_i<=d_i q`. An interval of mass `M>=5` instead
gives `D_i-3A>0`, since `(1-14a)M-4A>=3/10`. After obtaining `M<=4`,
a site of multiplicity at least three gives
`D_i-2q>=3A-56a>=97/40>0`. Both contradict optimality. The denominator's
double-to-single decrement is **three**, so blind simultaneous clipping
does not reproduce the argument.

This removes high multiplicity as a separate way to lower the small-notch
real floor, including `a=lambda eta^3` at sufficiently small width for
each fixed `lambda>0`. It leaves arbitrary total cardinality, arbitrarily
small gaps within the local mass cap, and possible failure of finite
attainment. It neither identifies a minimizing mixed configuration nor
extends to nonreal sites, where the positive pair estimates fail.
