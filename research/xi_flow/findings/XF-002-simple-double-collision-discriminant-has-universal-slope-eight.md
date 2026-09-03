# XF-002 — a simple double collision has an analytic discriminant with universal slope eight

**Status:** `EXACT-DERIVED` + `CLASSICAL-MECHANISM` for the local collision geometry of the Rodgers--Tao Xi-flow normalization. The analytic-discriminant mechanism is standard local analytic algebra; the durable line-specific result is the exact normalization and its consequence for collision-safe Xi-flow coordinates.

## 1. Claim

Let `E(t,z)` be real on the real axis, jointly analytic near a real point `(t_*,z_*)`, and solve the Rodgers--Tao backward heat equation

\[
E_t+E_{zz}=0.
\]

Assume `(t_*,z_*)` is a **simple double collision**:

\[
E(t_*,z_*)=E_z(t_*,z_*)=0,
\qquad E_{zz}(t_*,z_*)\neq 0.
\]

Then the two local zeros, although individually only Puiseux-analytic through the collision, admit two symmetric analytic coordinates: their center and their squared separation. More precisely, after writing `\tau=t-t_*` and `w=z-z_*`, the local Weierstrass quadratic can be written uniquely as

\[
E(t,z)=U(\tau,w)\bigl(w^2+b(\tau)w+c(\tau)\bigr),
\]

with `U(0,0)\neq0` and analytic `b,c` satisfying `b(0)=c(0)=0`. Its discriminant

\[
D(\tau):=b(\tau)^2-4c(\tau)
\]

is analytic through the collision and obeys the universal first-order law

\[
\boxed{D(0)=0,\qquad D'(0)=8.}
\]

Because the two roots are

\[
w_\pm(\tau)=\frac{-b(\tau)\pm\sqrt{D(\tau)}}{2},
\]

one has exactly

\[
(w_+(\tau)-w_-(\tau))^2=D(\tau)=8\tau+O(\tau^2).
\]

For real `\tau`, the coefficients are real. Hence, for sufficiently small nonzero `\tau`, the pair is real for `\tau>0` and a nonreal conjugate pair for `\tau<0`. Thus every simple double collision in this normalization is locally oriented in the same direction: increasing heat-flow time opens the collision into two real zeros.

## 2. Derivation from the PDE

Set

\[
A:=E_{zz}(t_*,z_*)\neq0.
\]

At `\tau=w=0`, differentiating the Weierstrass factorization twice in `w` gives

\[
A=2U(0,0),
\qquad U(0,0)=\frac A2.
\]

Now evaluate at `w=0`. Since `b(0)=c(0)=0`,

\[
E_t(t_*,z_*)=U(0,0)c'(0).
\]

The backward heat equation gives

\[
E_t(t_*,z_*)=-E_{zz}(t_*,z_*)=-A,
\]

so

\[
c'(0)=\frac{-A}{A/2}=-2.
\]

Since `b(0)=0`, differentiating the discriminant yields

\[
D'(0)=2b(0)b'(0)-4c'(0)=8.
\]

No zero labelling, bounded root velocity, global product over zeros, or separation from the remaining zero set is needed for this calculation. It uses only the local order-two Weierstrass factor and the exact backward heat equation.

## 3. Exact matched control and consistency with XF-001

The polynomial

\[
F(t,z)=z^2-2t
\]

is an exact solution of the same backward heat equation. Its Weierstrass polynomial already has `b(t)=0`, `c(t)=-2t`, hence

\[
D(t)=8t.
\]

Its roots are `\pm\sqrt{2t}` for `t>0` and `\pm i\sqrt{-2t}` for `t<0`. This simultaneously realizes the universal discriminant slope and the square-root velocity singularity established in XF-001.

There is therefore no contradiction between the two findings. The **individual roots** have divergent speed `\asymp |t-t_*|^{-1/2}`, while the **symmetric squared gap** is analytic with finite nonzero derivative. The singularity is unavoidable in branch coordinates but disappears after passing to the local discriminant.

## 4. Relation to real-rooted zero dynamics

Rodgers--Tao, building on Csordas--Smith--Varga, record that in the simple real-rooted regime `\Lambda<t\le0` the Xi-flow zeros satisfy

\[
\partial_t x_k(t)=2\sum_{j\ne k}\frac{1}{x_k(t)-x_j(t)}.
\]

Formally isolating an adjacent pair with gap `g=x_{k+1}-x_k` gives the singular leading term

\[
g'=\frac4g+O(g),
\]

and therefore

\[
(g^2)'=8+O(g^2).
\]

This agrees exactly with the local Weierstrass calculation. The Weierstrass proof is stronger for collision analysis because it does not require extending the simple-zero ODE to the singular endpoint or controlling the infinite interaction sum there.

## 5. Consequence for collision-safe variables

XF-001 showed that branchwise root tubes cannot assume bounded root speed through a collision. The present calculation identifies the smallest symmetric replacement that survives that obstruction:

\[
\boxed{q(t):=(z_+(t)-z_-(t))^2}
\]

is locally analytic at a simple double collision and, in Rodgers--Tao time, satisfies `q'(t_*)=8`.

Equivalently, `q/8` is a local analytic time coordinate through the collision. The pair center

\[
m(t):=\frac{z_+(t)+z_-(t)}2=-\frac{b(t)}2
\]

is analytic as well. Thus the pair can be represented across the collision by `(m,q)` without selecting a square-root branch.

This does **not** prove that any positivity, energy, or Lyapunov functional propagates through a collision. It does narrow the repair surface left by XF-001: a collision bridge based only on symmetric polynomial data need not inherit the nonintegrable `|\dot z|^2\asymp |t-t_*|^{-1}` cost merely from the local root branching. Any remaining singularity must come from the chosen functional or from interaction with the rest of the zero configuration, not from the intrinsic regularity of the local discriminant.

## 6. Prior-art and novelty boundary

Weierstrass preparation, discriminants of analytic polynomial families, and square-root/Puiseux splitting at a simple double root are classical. The zero-motion equation in the real-rooted Xi-flow regime is also classical in the de Bruijn--Newman literature and is stated explicitly in Rodgers--Tao, *The de Bruijn--Newman constant is non-negative* (Forum Math. Pi 8 (2020), e6), building on Csordas--Smith--Varga.

Recent polynomial heat-flow work, such as Hall--Ho, *The heat flow conjecture for polynomials and random matrices* (Letters in Mathematical Physics 115 (2025), 60), likewise treats root dynamics as regular only before singularities form; it does not turn collision regularity into an Xi-specific RH mechanism.

No novelty is claimed for analytic discriminants themselves. The reusable Mathia contribution is the exact collision-normalized identity `D'(t_*)=8` for the Xi-flow PDE and the resulting classification of `(center, squared gap)` as collision-safe local coordinates that pass the exact `z^2-2t` falsification control from XF-001.

## 7. Boundary conditions and decisive next test

The result requires a double zero of exact multiplicity two, equivalently `E_{zz}(t_*,z_*)\ne0`. It does not describe a triple or higher collision, simultaneous interacting collisions at the same spatial point, or the global behavior of the infinite zero system. It also gives no upper bound on `\Lambda` by itself: the same local normal form occurs in many non-Xi heat flows with positive transition time.

The decisive next test for a proposed collision-safe barrier is therefore stricter than merely replacing `z_\pm` by `D`. Construct the barrier in symmetric local coordinates, verify it on `z^2-2t`, and then show that the terms coupling `(m,D)` to the exterior zero configuration remain locally integrable and have a sign or coercivity property that is special to the Xi flow. Failure of that exterior-control step would show that discriminant regularization removes only the coordinate singularity, not the substantive obstruction.

## 8. Consequence for `xi_flow`

The collision frontier is now more precise. Branchwise motion is singular, but the collision itself is not singular in every coordinate. At a simple double collision the exact backward heat equation canonically supplies an analytic squared-gap coordinate with universal positive slope. Future Xi-flow barrier, entropy, or local-to-global arguments should therefore be tested first in `(center, discriminant)` variables; if they still require a nonintegrable coefficient there, the obstruction is structural rather than an artefact of root labelling.
